from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass
from typing import Any, List, Optional

import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# CRITICAL: load .env with override=True so the file ALWAYS wins over any
# stale OS-level GEMINI_API_KEY (Windows User/Machine env vars, inherited
# terminal env, etc.). Without override, an old blocked key in the terminal
# environment silently beats the new key in .env.
load_dotenv(override=True)
# Also search parent dirs (repo root) in case server runs from elsewhere.
_dotenv_path = find_dotenv(usecwd=True)
if _dotenv_path:
    load_dotenv(_dotenv_path, override=True)

from src.chat.mcp_client import MCPClient
from src.models.message import Message

logger = logging.getLogger(__name__)

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------

SYSTEM_PROMPT = """You are a Todo assistant.

Rules:
- You MUST use the provided tools for all task operations (add/list/update/complete/delete).
- Never fabricate task IDs. To reference an existing task, call list_tasks first and use the returned ID.
- For create, only send title (required) and description (optional). Ignore any other fields.
- After tool execution, respond with a friendly confirmation and results.
- If a tool fails, explain the error clearly.
"""

# --------------------------------------------------
# CONTEXT
# --------------------------------------------------

@dataclass
class ChatRunContext:
    user_id: str
    mcp: MCPClient
    jwt_token: str

# --------------------------------------------------
# GEMINI TOOL SCHEMAS
# --------------------------------------------------

# NOTE: google-generativeai 0.8.x + google-ai-generativelanguage 0.6.x requires
# "type_" (not "type") in parameter declarations. Keep in sync with SDK version.

ADD_TASK_TOOL = {
    "name": "add_task",
    "description": "Add a new todo task",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "title": {"type_": "STRING", "description": "Task title (required)"},
            "description": {"type_": "STRING", "description": "Optional task description"},
        },
        "required": ["title"],
    },
}

LIST_TASKS_TOOL = {
    "name": "list_tasks",
    "description": "List todo tasks",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "filter_completed": {"type_": "BOOLEAN", "description": "Filter by completion status"},
        },
    },
}

UPDATE_TASK_TOOL = {
    "name": "update_task",
    "description": "Update an existing task",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "task_id": {"type_": "STRING", "description": "ID of the task to update"},
            "title": {"type_": "STRING", "description": "New title"},
            "description": {"type_": "STRING", "description": "New description"},
        },
        "required": ["task_id"],
    },
}

COMPLETE_TASK_TOOL = {
    "name": "complete_task",
    "description": "Mark a task as completed",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "task_id": {"type_": "STRING", "description": "ID of the task to complete"},
        },
        "required": ["task_id"],
    },
}

DELETE_TASK_TOOL = {
    "name": "delete_task",
    "description": "Delete a task",
    "parameters": {
        "type_": "OBJECT",
        "properties": {
            "task_id": {"type_": "STRING", "description": "ID of the task to delete"},
        },
        "required": ["task_id"],
    },
}

TOOLS = [
    ADD_TASK_TOOL,
    LIST_TASKS_TOOL,
    UPDATE_TASK_TOOL,
    COMPLETE_TASK_TOOL,
    DELETE_TASK_TOOL,
]

MAX_TOOL_ROUNDS = 5

# Model fallback chain (free-tier friendly order, newest first):
# Google's 404 hints say 2.5-lite is retired for new users - use 3.5+ generations.
GEMINI_MODEL_CHAIN = [
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-flash-latest",
]


# --------------------------------------------------
# GEMINI CONFIGURATION
# --------------------------------------------------

def configure_gemini(preferred_model: Optional[str] = None):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    # Observability: log which key is loaded (prefix only) so stale/old-key
    # issues are visible in server logs immediately.
    logger.info(f"Gemini key loaded: {api_key[:8]}... (len={len(api_key)})")

    genai.configure(api_key=api_key)

    model_name = preferred_model or GEMINI_MODEL_CHAIN[0]
    logger.info(f"Using Gemini model: {model_name}")

    return genai.GenerativeModel(
        model_name=model_name,
        system_instruction=SYSTEM_PROMPT,
        tools=TOOLS,
    )

# --------------------------------------------------
# MAIN CHAT RUNNER
# --------------------------------------------------

async def run_chat_agent(
    user_id: str,
    conversation_id: str,
    user_message: str,
    history: Optional[List[Message]] = None,
    jwt_token: str = "",
) -> dict[str, Any]:

    mcp_client = MCPClient(jwt_token=jwt_token)
    ctx = ChatRunContext(user_id=user_id, mcp=mcp_client, jwt_token=jwt_token)

    # Track which model index we start with (for quota fallback retries)
    chain_idx = 0
    last_error: Optional[Exception] = None

    try:
        while chain_idx < len(GEMINI_MODEL_CHAIN):
            try:
                return await _run_with_model(
                    GEMINI_MODEL_CHAIN[chain_idx],
                    user_id, conversation_id, user_message, history, ctx,
                )
            except Exception as e:
                msg = str(e)
                # Quota/rate errors -> try next model in chain
                if ("429" in msg or "quota" in msg.lower() or "RESOURCE_EXHAUSTED" in msg) and chain_idx < len(GEMINI_MODEL_CHAIN) - 1:
                    logger.warning(f"Model {GEMINI_MODEL_CHAIN[chain_idx]} quota hit ({msg[:80]}); falling back to {GEMINI_MODEL_CHAIN[chain_idx + 1]}")
                    chain_idx += 1
                    continue
                raise
        raise last_error or RuntimeError("All Gemini models exhausted")
    finally:
        await mcp_client.aclose()


async def _run_with_model(
    model_name: str,
    user_id: str,
    conversation_id: str,
    user_message: str,
    history: Optional[List[Message]],
    ctx: ChatRunContext,
) -> dict[str, Any]:
    model = configure_gemini(preferred_model=model_name)

    chat = model.start_chat(history=[])

    # Add conversation history if present (as plain text turns)
    if history:
        for msg in history:
            chat.send_message(f"{msg.role.capitalize()}: {msg.content}")

    # Send user message
    response = chat.send_message(user_message)

    # --------------------------------------------------
    # MULTI-ROUND TOOL CALL LOOP
    # --------------------------------------------------
    # Gemini may request tools multiple times before producing a final
    # text answer (e.g. list_tasks -> delete_task). Loop until a plain
    # text response arrives or the safety cap is hit.

    rounds = 0
    while rounds < MAX_TOOL_ROUNDS:
        candidate = response.candidates[0]
        parts = candidate.content.parts or []

        function_calls = [p for p in parts if getattr(p, "function_call", None)]

        if not function_calls:
            break  # Plain text answer

        rounds += 1

        # Execute every requested tool call in order
        response_parts = []
        for part in function_calls:
            fn = part.function_call
            tool_name = fn.name
            tool_args = {k: v for k, v in dict(fn.args).items() if not k.startswith("_")}

            logger.info(f"Gemini requested tool: {tool_name} {tool_args}")

            # Call MCP tool (JWT injected server-side, never from the model)
            tool_result = await ctx.mcp.call_tool(tool_name, tool_args)

            # Serialize result for Gemini (drop internals)
            result_payload = {
                "success": tool_result.success,
            }
            if tool_result.data is not None:
                result_payload["data"] = tool_result.data
            if tool_result.error is not None:
                result_payload["error"] = tool_result.error

            # Correct FunctionResponse format for google.generativeai
            response_parts.append({
                "function_response": {
                    "name": tool_name,
                    "response": result_payload,
                }
            })

        # Send ALL tool results back in one turn
        followup = chat.send_message(response_parts)
        response = followup

    if rounds >= MAX_TOOL_ROUNDS:
        logger.warning(f"Tool round cap ({MAX_TOOL_ROUNDS}) reached for user {user_id}")

    # --------------------------------------------------
    # FINAL TEXT RESPONSE
    # --------------------------------------------------
    final_text = response.text.strip() if response.candidates else "Sorry, I could not process that."

    return {
        "response_text": final_text,
        "conversation_id": conversation_id,
    }

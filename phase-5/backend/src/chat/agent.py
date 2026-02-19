from __future__ import annotations

import os
import logging
from dataclasses import dataclass
from typing import Any, Optional, List

import google.generativeai as genai

from src.chat.mcp_client import MCPClient
from src.models.message import Message

logger = logging.getLogger(__name__)

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------

SYSTEM_PROMPT = """You are a Todo assistant.

Rules:
- You MUST use the provided tools for all task operations (add/list/update/complete/delete).
- Do not modify tasks in any other way.
- When the user asks for a task operation, call the correct tool.
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

# --------------------------------------------------
# GEMINI TOOL SCHEMAS
# --------------------------------------------------

ADD_TASK_TOOL = {
    "name": "add_task",
    "description": "Add a new todo task",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
        },
        "required": ["title"],
    },
}

LIST_TASKS_TOOL = {
    "name": "list_tasks",
    "description": "List todo tasks",
    "parameters": {
        "type": "object",
        "properties": {
            "filter_completed": {"type": "boolean"},
        },
    },
}

UPDATE_TASK_TOOL = {
    "name": "update_task",
    "description": "Update an existing task",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {"type": "string"},
            "title": {"type": "string"},
            "description": {"type": "string"},
        },
        "required": ["task_id"],
    },
}

COMPLETE_TASK_TOOL = {
    "name": "complete_task",
    "description": "Mark a task as completed",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {"type": "string"},
        },
        "required": ["task_id"],
    },
}

DELETE_TASK_TOOL = {
    "name": "delete_task",
    "description": "Delete a task",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {"type": "string"},
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

# --------------------------------------------------
# GEMINI CONFIGURATION
# --------------------------------------------------

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    genai.configure(api_key=api_key)

    return genai.GenerativeModel(
        model_name="gemini-2.5-flash",
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
) -> dict[str, Any]:

    model = configure_gemini()
    mcp_client = MCPClient()
    ctx = ChatRunContext(user_id=user_id, mcp=mcp_client)

    try:
        chat = model.start_chat(history=[])

        # Add conversation history if present
        if history:
            for msg in history:
                chat.send_message(f"{msg.role.capitalize()}: {msg.content}")

        # Send user message
        response = chat.send_message(user_message)

        candidate = response.candidates[0]
        part = candidate.content.parts[0]

        # --------------------------------------------------
        # TOOL CALL HANDLING
        # --------------------------------------------------
        if hasattr(part, "function_call") and part.function_call:
            fn = part.function_call
            tool_name = fn.name
            tool_args = dict(fn.args)

            logger.info(f"Gemini requested tool: {tool_name} {tool_args}")

            # Call MCP tool
            tool_result = await ctx.mcp.call_tool(tool_name, tool_args)

            # Send tool result back to Gemini
            followup = chat.send_message({
                "role": "tool",
                "name": tool_name,
                "content": str(tool_result.__dict__),
            })

            return {
                "response_text": followup.text.strip(),
                "conversation_id": conversation_id,
            }

        # --------------------------------------------------
        # NORMAL RESPONSE
        # --------------------------------------------------
        return {
            "response_text": response.text.strip(),
            "conversation_id": conversation_id,
        }

    finally:
        await mcp_client.aclose()

import logging
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session

from src.utils.errors import create_error_response
from src.api.dependencies.auth import get_current_user, TokenUser
from src.chat.agent import run_chat_agent
from src.chat.persistence import append_message, load_or_create_conversation, get_conversation_history
from src.chat.schemas import ChatRequest, ChatResponse
from src.db.session import get_session


def _extract_bearer_token(request) -> str:
    """Extract raw JWT from Authorization header or Better Auth session cookie."""
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return auth[7:]
    return request.cookies.get("better-auth-session") or ""


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat(
    payload: ChatRequest,
    request: Request,
    user_id: str,
    current_user: TokenUser = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> ChatResponse:
    try:
        logger.info(f"Processing chat request for user {user_id}")

        # Authenticated user (from JWT) must match the path user id
        if str(current_user.user_id) != user_id:
            raise HTTPException(status_code=403, detail="Access denied: user ID mismatch")

        convo = load_or_create_conversation(session, user_id)
        logger.debug(f"Loaded/created conversation {convo.id} for user {user_id}")

        # Get conversation history for context (implementing US2 - resume conversation after restart)
        # QUOTA GUARD: trim to the last 8 messages (4 user+assistant turns).
        # Every history message = 1 extra Gemini request on replay, which burns
        # the free-tier 5-15 RPM limits in a few chats.
        history = get_conversation_history(session, convo.id)[-8:]
        logger.debug(f"Fetched {len(history)} history messages for conversation {convo.id}")

        # Append user message to conversation before running agent
        user_msg = append_message(session, convo.id, role="user", content=payload.message)
        logger.debug(f"Saved user message to conversation {convo.id}")

        # Run the agent to process the request with conversation history context
        # JWT is passed server-side so MCP tools can authenticate the user
        agent_response = await run_chat_agent(
            user_id=user_id,
            conversation_id=str(convo.id),
            user_message=payload.message,
            history=history,  # Pass history for context-aware responses
            jwt_token=_extract_bearer_token(request),
        )

        # Save the assistant's response to the conversation
        assistant_msg = append_message(session, convo.id, role="assistant", content=agent_response["response_text"])
        logger.debug(f"Saved assistant response to conversation {convo.id}")

        logger.info(f"Successfully processed chat request for user {user_id}, conversation {convo.id}")

        return ChatResponse(
            conversation_id=agent_response["conversation_id"],
            assistant_message=agent_response["response_text"]
        )
    except HTTPException:
        logger.warning(f"HTTP exception in chat for user {user_id}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in chat for user {user_id}: {e}", exc_info=True)
        # Standardize error response format to match backend/src/api/main.py:create_error_response
        raise HTTPException(status_code=500, detail=str(e))
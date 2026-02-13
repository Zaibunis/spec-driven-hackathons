# Quickstart Guide: AI Chat Agent & Integration

**Feature**: AI Chat Agent & Integration
**Date**: 2026-01-20
**Branch**: 001-ai-chat-agent

## Overview

This guide provides the essential information to implement the AI-powered chatbot for natural language todo management. The implementation uses OpenAI Agents SDK, integrates with MCP tools, and maintains persistent conversation memory in the database.

## Prerequisites

- Python 3.11+
- Node.js 18+ (for frontend)
- Next.js 16+ with App Router
- FastAPI
- SQLModel
- OpenAI Agents SDK
- Neon Serverless PostgreSQL
- Better Auth with JWT

## Environment Setup

### Backend Configuration

1. **Install Dependencies**:
   ```bash
   pip install openai fastapi uvicorn sqlmodel python-multipart
   ```

2. **Environment Variables**:
   ```bash
   # OpenAI configuration
   OPENAI_API_KEY=your_openai_api_key_here

   # Database configuration
   DATABASE_URL=postgresql+asyncpg://username:password@host:port/database

   # Auth configuration
   BETTER_AUTH_SECRET=your_better_auth_secret
   ```

### Frontend Configuration

1. **Install Dependencies**:
   ```bash
   npm install @types/node @types/react openai
   ```

2. **Environment Variables**:
   ```bash
   NEXT_PUBLIC_OPENAI_API_KEY=your_openai_api_key_here
   ```

## Implementation Steps

### 1. Database Models

Create the data models in `backend/src/models/`:

- `conversation.py` - Conversation entity with user relationship
- `message.py` - Message entity with sender_type and content
- Update existing `user.py` if needed

### 2. Database Services

Create services in `backend/src/services/`:

- `conversation_service.py` - Handle conversation creation, retrieval, and updates
- `ai_agent_service.py` - Integrate with OpenAI Agents SDK
- `mcp_tool_integration.py` - Interface with MCP tools for todo operations

### 3. API Endpoints

Create the chat API in `backend/src/api/chat_api.py`:

- `POST /api/chat/send` - Process user messages through AI agent
- `GET /api/chat/history/{conversation_id}` - Retrieve conversation history
- `GET /api/chat/conversations` - List user's conversations
- `POST /api/chat/conversations` - Create new conversation

### 4. Frontend Components

Create chat interface components in `frontend/src/components/chat/`:

- `ChatInterface.tsx` - Main chat container component
- `MessageDisplay.tsx` - Component to display messages
- `MessageInput.tsx` - Component for message input and submission

### 5. Service Integration

- `frontend/src/services/chat_api_client.ts` - API client for chat endpoints
- Update existing authentication integration to pass JWT tokens

## Key Implementation Details

### AI Agent Configuration

1. Initialize OpenAI Agent with proper tools:
   ```python
   # In ai_agent_service.py
   from openai import OpenAI

   client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

   # Define tools for todo operations using MCP integration
   tools = [
       # Define MCP tools for todo operations
   ]
   ```

2. Ensure the agent operates statelessly by retrieving conversation context from database for each request.

### MCP Tool Integration

1. Create MCP tools that follow the schema-defined requirements
2. Ensure all operations are scoped to the authenticated user
3. Implement proper error handling for tool failures

### Authentication Flow

1. Frontend extracts JWT from Better Auth session
2. Attaches JWT to Authorization header for chat API requests
3. Backend validates JWT and extracts user identity
4. All operations are scoped to the authenticated user

## Testing Strategy

### Backend Tests
- Test conversation creation and retrieval
- Test message processing through AI agent
- Test user data isolation
- Test error handling for AI processing failures

### Frontend Tests
- Test chat interface functionality
- Test API client integration
- Test authentication flow with JWT tokens

## Deployment Notes

1. Ensure environment variables are properly configured in deployment environment
2. Database migrations must include new Conversation and Message tables
3. Verify that JWT authentication works properly in deployed environment
4. Monitor AI API usage costs and implement appropriate rate limiting if needed
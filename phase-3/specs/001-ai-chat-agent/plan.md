# Implementation Plan: AI Chat Agent & Integration

**Branch**: `001-ai-chat-agent` | **Date**: 2026-01-20 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/001-ai-chat-agent/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of an AI-powered chatbot for natural language todo management using OpenAI Agents SDK. The system integrates with the existing Chatkit frontend and connects to a stateless FastAPI chat endpoint that processes messages through an AI agent. The agent uses MCP tools exclusively for todo operations while maintaining persistent conversation memory in the database. The architecture ensures user isolation and follows stateless design principles with conversation context rebuilt from database on each request.

## Technical Context

**Language/Version**: Python 3.11, JavaScript/TypeScript (Next.js 16+)
**Primary Dependencies**: FastAPI, OpenAI Agents SDK, Better Auth, SQLModel, Neon PostgreSQL
**Storage**: Neon Serverless PostgreSQL for conversation and message persistence
**Testing**: pytest for backend, Jest for frontend
**Target Platform**: Web application (Linux server deployment)
**Project Type**: Web application (separate frontend and backend)
**Performance Goals**: <5 second response time for AI processing, 90%+ intent recognition accuracy
**Constraints**: <5 second response time, 95% uptime, stateless design with no in-memory conversation state
**Scale/Scope**: Single user conversations, persistent across sessions, MCP tool integration

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] Spec exists and includes acceptance scenarios + edge cases sufficient for
      autonomous execution.
- [X] All user-facing actions are authenticated; backend endpoints require JWT and
      return 401 on missing/invalid token.
- [X] Data access is scoped to the authenticated user; cross-user access is prevented.
- [X] Stack constraints honored (Next.js App Router, FastAPI, SQLModel, Neon, Better
      Auth JWT with `Authorization: Bearer <token>`).
- [X] Backend remains stateless; REST conventions + status codes are explicit.
- [X] Work will be executed via Claude Code workflows (no manual coding) and a PHR will
      be recorded for this prompt.
- [X] AI logic implemented using OpenAI Agents SDK and MCP tools.
- [X] MCP tools are stateless and schema-defined.
- [X] Conversation context is rebuilt from database each request.
- [X] All AI actions are traceable and persisted in database.

## Project Structure

### Documentation (this feature)

```text
specs/001-ai-chat-agent/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── conversation.py
│   │   ├── message.py
│   │   └── user.py
│   ├── services/
│   │   ├── ai_agent_service.py
│   │   ├── conversation_service.py
│   │   └── mcp_tool_integration.py
│   ├── api/
│   │   └── chat_api.py
│   └── core/
│       ├── config.py
│       └── dependencies.py

frontend/
├── src/
│   ├── components/
│   │   └── chat/
│   │       ├── ChatInterface.tsx
│   │       ├── MessageDisplay.tsx
│   │       └── MessageInput.tsx
│   ├── services/
│   │   └── chat_api_client.ts
│   ├── types/
│   │   ├── conversation.ts
│   │   └── message.ts
│   └── lib/
│       └── utils.ts
```

**Structure Decision**: Web application structure selected with separate backend and frontend directories. Backend contains AI agent service, conversation models, and chat API. Frontend contains chat interface components and API client integration.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | None | None |
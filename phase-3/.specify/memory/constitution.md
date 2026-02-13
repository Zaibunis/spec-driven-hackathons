# Todo Full-Stack Web Application Constitution
<!--
Sync Impact Report
- Version change: 1.0.0 → 1.1.0
- Modified principles: Updated AI Logic Implementation Standards with agent-first design and clear separation; Enhanced Tool-driven AI with schema-defined requirement and context rebuilding; Updated Stateless server architecture with FastAPI endpoint requirement; Enhanced Database-backed conversation memory with resumable conversations and traceability
- Added sections: None
- Removed sections: None
- Templates requiring updates:
  - ✅ updated: .specify/templates/plan-template.md
  - ✅ updated: .specify/templates/spec-template.md
  - ✅ updated: .specify/templates/tasks-template.md
  - ✅ updated: .claude/commands/sp.constitution.md
- Follow-up TODOs:
  - None
-->

## Core Principles

### Spec-driven development
- No implementation work may begin without an explicit, written specification.
- Every feature MUST follow the workflow: spec → plan → tasks → implement.
- Specs MUST define acceptance scenarios and error/edge cases that are sufficient for
  autonomous agent execution.

### Security by default (auth + user isolation)
- Every user-facing action MUST be authenticated and authorized.
- All backend API endpoints MUST require a valid JWT and return `401 Unauthorized` when
  missing/invalid.
- Authenticated user identity MUST be derived from the JWT only.
- All task data access MUST be scoped to the authenticated user; cross-user access is
  forbidden.
- Token expiration MUST be respected.
- Secrets/tokens MUST NOT be hardcoded; configuration MUST use environment variables.

### Deterministic behavior
- The system MUST be stateless on the backend; requests are fully determined by
  `(request body, headers, authenticated user, database state)`.
- The same inputs MUST produce the same outputs (including ordering) unless persisted
  state has changed.

### Separation of concerns
- Frontend (Next.js) and backend (FastAPI) responsibilities MUST remain distinct.
- Authentication is handled by Better Auth on the frontend; the backend verifies JWTs
  and enforces authorization.
- Database access MUST be encapsulated through SQLModel/SQLAlchemy patterns (no raw,
  ad-hoc access paths that bypass authorization constraints).

### Agentic implementation (no manual coding)
- Changes are executed through Claude Code workflows and reviewed iteratively.
- Significant work MUST be routed through the appropriate specialized agent:
  - Auth: `auth-flow-engineer`
  - Backend: `fastapi-backend-engineer`
  - DB: `neon-db-architect`
  - Frontend: `nextjs-ui-builder`
- A Prompt History Record (PHR) MUST be created for every user prompt.

### Authoritative stack + explicit contracts
- The authoritative stack is:
  - Frontend: Next.js 16+ (App Router)
  - Backend: Python FastAPI
  - ORM: SQLModel
  - Database: Neon Serverless PostgreSQL
  - Authentication: Better Auth (JWT issuance supported)
- System communication MUST be RESTful JSON.
- REST conventions MUST be followed consistently, including correct HTTP status codes.
- API behavior MUST be explicit, testable, and unambiguous.

### AI Logic Implementation Standards
- AI logic MUST be implemented using OpenAI Agents SDK.
- Task operations MUST be exposed via Official MCP SDK.
- AI agents MUST invoke MCP tools for all task actions.
- MCP tools MUST be stateless and deterministic.
- Conversation state MUST be persisted in PostgreSQL database.
- Agent-first design MUST be used with stateless chat and tool execution.
- Clear separation MUST be maintained: UI → Agent → MCP Tools → Database.

### Natural language as a first-class interface
- Natural language processing MUST be treated as a primary interaction method for users.
- The AI chatbot interface MUST interpret user intentions expressed in natural language.
- Todo management operations MUST be accessible through conversational commands.

### Tool-driven AI
- AI agents MUST act only via MCP (Model Context Protocol) tools for all actions.
- All AI decisions MUST result in specific, well-defined tool invocations.
- Agent behavior MUST be deterministic and reproducible through tool sequences.
- MCP tools MUST be stateless and schema-defined.
- Conversation context MUST be rebuilt from database each request.

### Stateless server architecture
- The server MUST remain fully stateless with no in-memory conversation state.
- All conversation context MUST be retrieved from persistent storage for each request.
- System scalability MUST be maintained through stateless design principles.
- FastAPI chat endpoint MUST be stateless.

### Database-backed conversation memory
- Conversation history MUST be persisted in PostgreSQL database.
- AI agents MUST retrieve conversation context from the database before processing.
- Conversation continuity MUST survive server restarts and scaling events.
- Conversations MUST be resumable after restart.
- All AI actions MUST be traceable and persisted.

## Constraints

- Frontend: Next.js 16+ with App Router
- Backend: FastAPI (Python) with SQLModel
- Database: Neon Serverless PostgreSQL
- Authentication: Better Auth with JWT
- Backend authorization:
  - Frontend calls FastAPI with `Authorization: Bearer <token>`
  - Backend verifies JWT signature with shared secret (`BETTER_AUTH_SECRET`)
  - Backend scopes all data to the authenticated user

Non-goals:
- Do not implement detection evasion, destructive payloads, or unauthorized security
  testing.

## Development Workflow & Quality Gates

- Workflow MUST be: spec → plan → tasks → implement.
- Plans and tasks MUST include clear, testable acceptance criteria.
- Minimal diffs: avoid unrelated refactors.
- Quality gates (must hold for every change):
  - All API endpoints are authenticated and enforce ownership checks.
  - Backend remains stateless.
  - Frontend is responsive and auth-aware.
  - Database integrity is preserved (constraints/relationships are correct).

## Governance

- This constitution supersedes other practices.
- Amendments MUST:
  - be documented in this file,
  - include the rationale and the implications,
  - include a migration plan if they change existing rules.
- Semantic versioning policy for this constitution:
  - MAJOR: backward-incompatible rule removals/redefinitions
  - MINOR: new principle/section added or materially expanded
  - PATCH: clarifications and non-semantic refinements
- Compliance expectations:
  - Reviews MUST verify authentication, authorization, and user isolation.
  - Work products MUST be traceable (spec/plan/tasks and PHR entries).

**Version**: 1.1.0 | **Ratified**: 2026-01-09 | **Last Amended**: 2026-01-20

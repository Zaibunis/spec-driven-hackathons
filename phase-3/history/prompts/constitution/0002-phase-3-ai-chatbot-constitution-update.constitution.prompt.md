---
id: 0002
title: "Phase-3-AI-Chatbot-constitution-update"
stage: constitution
date: 2026-01-20
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: unknown
command: /sp.constitution
labels: ["constitution","ai","mcp-tools","openai-agents","stateless-architecture"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
  - .claude/commands/sp.constitution.md
tests:
  - null
---

## Prompt

```text
Project Extension: Phase-3 - AI-Powered Todo Chatbot

Core Addition:
-Agent-first design using OpenAI Agents SDK
-Stateless chat and tool execution
-All task actions executed only via MCP tools
-Clear separation: UI -> Agent -> MCP Tools -> Database

Key standards:
-Agent must not access the database directly
-MCP tools must be stateless and schema-defined
-Conversation context rebuilt from database each request
-All AI actions traceable and persisted
-Phase-2 auth and user isolation rules remain enforced

Constraints:
-Use OpenAI Agents SDK and Official MCP SDK
-Stateless FastAPI chat endpoint
-Persist conversations and messages in Neon PostgreSQL
-No manual coding; Claude Code only

Success Criteria:
-Users manage todos via natural language
-Agent correctly invokes MCP tools
-Conversations resumed after restart
-System remains secure and stateless
```

## Response snapshot

- Updated the constitution to version 1.1.0, incorporating Phase-3 requirements for the AI-Powered Todo Chatbot, including agent-first design with OpenAI Agents SDK, stateless chat execution, and MCP tools integration.
- Enhanced AI Logic Implementation Standards with clear separation (UI → Agent → MCP Tools → Database) and stateless requirements.
- Strengthened Tool-driven AI principles with schema-defined MCP tools and database context rebuilding requirements.
- Updated Database-backed conversation memory with resumable conversations and traceability requirements.
- Propagated changes to dependent templates: plan-template.md, spec-template.md, tasks-template.md, and sp.constitution.md.

## Outcome

- ✅ Impact: Constitution now fully supports Phase-3 AI chatbot requirements with proper MCP tool integration and stateless architecture.
- 🧪 Tests: Not run (docs/template edits only).
- 📁 Files: Updated constitution and all related templates.
- 🔁 Next prompts: Run `/sp.specify` for Phase-3 AI chatbot feature specifications.
- 🧠 Reflection: Constitution now properly captures AI/MCP tool requirements for the agent-first architecture.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not applicable.
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): None needed - constitution now fully supports Phase-3 requirements.
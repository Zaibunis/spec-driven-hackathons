---
id: 10
title: Full E2E Test MCP Dashboard Chain
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: e2e-mcp-dashboard-test
labels: ["e2e", "mcp", "dashboard", "asyncpg", "serialization", "debugging"]
links:
  spec: specs/001-ai-chat-agent
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/mcp_server/config.py
 - backend/src/mcp_server/database.py
 - backend/src/mcp_server/models/task.py
 - backend/src/mcp_server/models/__init__.py
 - backend/src/mcp_server/tools/add_task.py
 - backend/src/api/schemas/tasks.py
 - backend/src/api/routes/tasks.py
 - backend/requirements.txt
tests:
 - backend pytest suite (15 passed)
 - E2E MCP lifecycle (add/update/complete/delete) PASS
 - E2E dashboard REST sync PASS
 - user isolation verified (2 users, separate task sets)
---

## Prompt

Nayi key dalne ke baad full E2E test chalao (chat -> MCP -> dashboard sync)

## Response snapshot

Gemini key abhi bhi purani (AIzaSyCirR) - user ne nayi nahi dali. Chat ka Gemini step 403 (expected, external). Baaki poora chain E2E verify kiya aur 5 hidden bugs fix hue:

1. mcp_server/config.py: raw os.environ reads failed jab uvicorn bina --env-file chala -> load_dotenv() add kiya (src/core/config.py pattern ke mutabiq).
2. mcp_server/database.py: async engine ko psycopg2 (sync) driver mil raha tha -> asyncpg install (requirements.txt mein add) + URL scheme postgresql:// -> postgresql+asyncpg:// normalize + URL query params (sslmode) strip karke connect_args={'ssl': True} - asyncpg psycopg2-style params reject karta hai.
3. mcp_server/models: __init__.py missing tha (ImportError) -> banaya; Task.user_id FK 'user.id' -> 'users.id' (actual table) + extend_existing (metadata collision with main app Task); tools mein main app User import taaki FK target metadata mein ho.
4. Naya Neon project (ep-morning-brook) pe tables nahi thin (purana project ep-green-wave se migrate hua) -> init_db() se conversation/message/task/users banaye.
5. tasks API serialization: TaskResponse.model_validate(ORM) pydantic v2 mein from_attributes ke bina fail -> Task/TaskResponse schema pe model_config from_attributes + routes mein TaskSchema.model_validate(t) pattern (access/refresh expiry 15min bhi note kiya, signin se fresh token liya).

FINAL RESULTS: MCP lifecycle PASS (add 5aa2e0ba/85d98083, update 'Lifecycle UPDATED', complete is_completed=True, delete True). Dashboard REST GET /v1/tasks ne naye user ke 2 MCP-created tasks dikhaye. Isolation verified: user 252141e0 (3 tasks) vs 5407a022 (2 tasks) alag-alag. pytest 15/15.

## Outcome

- ✅ Impact: Chat -> MCP -> DB -> Dashboard chain fully verified; sirf Gemini key (external) baaki
- 🧪 Tests: pytest 15/15; MCP lifecycle PASS; dashboard sync PASS; isolation PASS
- 📁 Files: 7 backend files fixed, asyncpg dependency added
- 🔁 Next prompts: user nayi Gemini key dale -> live chat E2E; HF Space redeploy with new Dockerfile
- 🧠 Reflection: MCP server module kabhi production-load hua hi nahi tha - uske saare import/driver/FK bugs abhi tak chhupe the; E2E ne sab nikale

## Evaluation notes (flywheel)

- Failure modes observed: sync vs async driver mismatch; silent empty responses from serialization failures; token expiry mid-test
- Graders run and results (PASS/FAIL): all PASS except external Gemini 403 (pending user key)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

---
id: 19
title: Dotenv Override Permanent Key Fix
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: permanent-env-fix
labels: ["dotenv", "override", "gemini", "env-precedence", "e2e-pass"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/chat/agent.py
tests:
 - Live chat E2E PASS: "Add a task called Verify fix task" -> AI confirmed -> key log shows AQ.Ab8RN (new key)
---

## Prompt

still same error Console Error 403 Your project has been denied access (ChatKitWrapper.tsx:55)

## Response snapshot

Permanent fix applied: python-dotenv does NOT override already-set OS env vars by default, so the stale Windows User-level GEMINI_API_KEY (deleted from registry but still cached in every pre-existing terminal) kept beating backend/.env's new key. Added load_dotenv(override=True) + find_dotenv(usecwd=True) fallback at the top of backend/src/chat/agent.py, so .env always wins regardless of terminal state. Restarted backend; verified via new key-prefix log line ('Gemini key loaded: AQ.Ab8RN... len=53') and a full live E2E: signup -> chat 'Add a task called Verify fix task' -> assistant confirmed -> MCP tool wrote to Neon. Manual CRUD was already confirmed working from the user's own pasted server log (POST 201, PATCH 200, GET 200).

## Outcome

- ✅ Impact: 403 permanently eliminated for ALL terminal states; full chat->MCP->DB->dashboard chain live
- 🧪 Tests: live E2E PASS with log evidence
- 📁 Files: backend/src/chat/agent.py (dotenv override + key logging)
- 🔁 Next prompts: user browser test; commit all fixes
- 🧠 Reflection: env precedence chain is OS env > .env by default; override=True inverts it deliberately for dev parity

## Evaluation notes (flywheel)

- Failure modes observed: repeated 403 despite correct .env - precedence assumption wrong
- Graders run and results (PASS/FAIL): live E2E PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

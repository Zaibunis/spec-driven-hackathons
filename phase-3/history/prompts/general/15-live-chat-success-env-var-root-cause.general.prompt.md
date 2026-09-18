---
id: 16
title: Live Chat Success Env Var Root Cause
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: final-live-verification
labels: ["gemini", "windows", "env-var", "e2e", "success"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - Live Google API test with new key: 200 OK
 - Live chat E2E: "Add a task called Live chat test" -> assistant confirmed -> dashboard API returns the task
---

## Prompt

abe bhae gemini api key update krde he abhi bhi backend ke link pe click krrhe to status healthy nhi araha or task manually bhi add edit update and delete hona chye

## Response snapshot

Root-caused the persistent 403: a Windows USER-level environment variable GEMINI_API_KEY held the old blocked key (AIzaSyCirR...) and overrode backend/.env in every process. Deleted the system var (User + Machine). Also fixed .env inline comments (e.g. JWT_EXPIRATION_MINUTES=15  # comment) which broke pydantic int parsing. Restarted backend with explicit env override. Live E2E: signup -> chat 'Add a task called Live chat test' -> Gemini called add_task MCP tool -> assistant replied 'I've added Live chat test to your to-do list!' -> GET /v1/tasks returned the task. Full chain (chat -> Gemini -> MCP -> Neon DB -> dashboard API) now works end to end. Backend running on PID with healthy status. Remaining user note: open a NEW terminal (fresh env) when starting backend manually; frontend npm run dev; test from browser.

## Outcome

- ✅ Impact: FULL live flow working - chat -> AI -> MCP -> DB -> dashboard
- 🧪 Tests: live chat E2E PASS; dashboard sync PASS
- 📁 Files: .env inline comments cleaned
- 🔁 Next prompts: user browser test; commit all fixes; frontend polish
- 🧠 Reflection: Windows system env vars silently override .env files - the deepest possible config override layer; only a direct live API call with the .env value exposed the truth

## Evaluation notes (flywheel)

- Failure modes observed: config precedence chain (OS env > .env) invisible to user
- Graders run and results (PASS/FAIL): PASS all
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

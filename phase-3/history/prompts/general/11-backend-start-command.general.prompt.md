---
id: 11
title: Backend Start Command Reference
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: backend-start-command
labels: ["backend", "uvicorn", "command", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests: []
---

## Prompt

backend ko start krne ki command

## Response snapshot

Provided canonical start command: `cd D:\Documents\phase\backend` then `python -m uvicorn src.main:app --env-file .env --host 0.0.0.0 --port 8000`. Emphasized `python -m uvicorn` (Device Guard blocks the .exe shim) and `--env-file .env` (required for DATABASE_URL/JWT_SECRET/GEMINI_API_KEY, including MCP tools). Included health check URL (/health), docs (/docs), and Ctrl+C to stop.

## Outcome

- ✅ Impact: Quick reference for daily backend startup
- 🧪 Tests: none (informational)
- 📁 Files: none
- 🔁 Next prompts: live chat E2E after new Gemini key
- 🧠 Reflection: same command as session-established runbook (PHR 4/5)

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

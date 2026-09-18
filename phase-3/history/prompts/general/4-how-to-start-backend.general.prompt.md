---
id: 4
title: How To Start Backend Server
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: explain-backend-startup
labels: ["backend", "fastapi", "uvicorn", "setup", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests: []
---

## Prompt

how to start backend

## Response snapshot

Documented backend startup paths: local dev via `cd backend && uvicorn src.main:app --reload --env-file .env` (loads required DATABASE_URL/JWT_SECRET/GEMINI_API_KEY/BETTER_AUTH_SECRET into environment, satisfying the new env-only secret policy), Docker (`docker build -t todo-backend ./backend` + `--env-file backend/.env`), docker-compose (backend on port 7860, requires root `.env` from `.env.example`), and Minikube (create `todo-backend-secrets` secret then apply manifest). Endpoints: app :8000, docs /docs, health /health.

## Outcome

- ✅ Impact: Operational runbook for backend startup in all 4 environments
- 🧪 Tests: none (informational)
- 📁 Files: none
- 🔁 Next prompts: start frontend; verify health endpoint; run full compose stack
- 🧠 Reflection: `--env-file` flag bridges pydantic Settings and os.environ requirements after secrets remediation

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

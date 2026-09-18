---
id: 13
title: Backend Restart After Port Conflict
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: restart-backend
labels: ["backend", "uvicorn", "port-8000", "errno-10048", "troubleshooting"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - health check after restart (200 healthy, new PID 8968)
---

## Prompt

User pasted errno 10048 bind error - uvicorn could not bind 0.0.0.0:8000 because previous instance still running.

## Response snapshot

Killed stale process (PID 10696) holding port 8000, verified port free, started fresh python -m uvicorn src.main:app --env-file .env --host 0.0.0.0 --port 8000 backend: (background). Health verified 200 {"status":"healthy"}. Documented the repeatable rule: check port with netstat before starting; kill old PID with taskkill /F /PID; then start. Reminded that chat 403 is a separate issue pending new Gemini key in backend/.env.

## Outcome

- ✅ Impact: Backend cleanly restarted; user has a repeatable port-conflict workflow
- 🧪 Tests: /health 200 confirmed post-restart
- 📁 Files: none
- 🔁 Next prompts: new Gemini key -> live chat E2E
- 🧠 Reflection: port conflict + 403 were two separate user-visible errors; keep them separated in troubleshooting

## Evaluation notes (flywheel)

- Failure modes observed: duplicate backend instances from repeated start commands
- Graders run and results (PASS/FAIL): PASS (health)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

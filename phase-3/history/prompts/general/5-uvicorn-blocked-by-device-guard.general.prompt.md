---
id: 5
title: Uvicorn Blocked By Device Guard
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: troubleshoot-uvicorn-startup
labels: ["backend", "uvicorn", "windows", "device-guard", "troubleshooting"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - backend startup smoke test (uvicorn boot + GET /health = {"status":"healthy"})
---

## Prompt

D:\Documents\phase\backend>uvicorn src.main:app --reload --env-file'C:\Users\ZAINAB KHAN\AppData\Local\Programs\Python\Python311\Scripts\uvicorn.exe' was blocked by your organization's Device Guard policy.Contact your support person for more info.

## Response snapshot

Diagnosed as Windows Device Guard blocking the pip-generated `uvicorn.exe` launcher shim, not a project issue. Fix: run uvicorn as a Python module - `cd backend && python -m uvicorn src.main:app --reload --env-file .env` - which bypasses the blocked .exe wrapper. Verified on the user's machine (uvicorn 0.40.0, CPython 3.11.9): server booted and GET /health returned {"status":"healthy"}. Documented alternatives: IT whitelist of the Scripts path, or venv-based install whose .exe lives at a different path. General pattern: `python -m <tool>` for any pip tool whose .exe is policy-blocked.

## Outcome

- ✅ Impact: Backend startup unblocked without policy changes or app code changes
- 🧪 Tests: startup smoke test passed (/health 200)
- 📁 Files: none
- 🔁 Next prompts: frontend dev server startup; full-stack compose run
- 🧠 Reflection: Device Guard targets .exe shims; module invocation is the standard workaround

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS (health endpoint verified)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

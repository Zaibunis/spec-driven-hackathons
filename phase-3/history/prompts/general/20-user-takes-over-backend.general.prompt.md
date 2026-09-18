---
id: 24
title: User Takes Over Backend Control
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: free-port-handover
labels: ["backend", "port-8000", "handover", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - port 8000 confirmed free after cleanup
---

## Prompt

mujhe bataa do na backend ki command apne pas chala ke rkha he command do me apne pas chala rha hun dimag kharab, or apne pas se band krdo backend

## Response snapshot

User frustrated by duplicate backend instances (mine in background vs theirs in terminal). Killed all my background uvicorn processes, verified port 8000 is fully free. Handed control to the user with the single canonical start command and a cheat-sheet: netstat to check port, taskkill to clear zombies, python -m uvicorn with --env-file to start. Health URL is the source of truth for whether backend is running.

## Outcome

- ✅ Impact: Clean handover; user owns backend lifecycle now
- 🧪 Tests: port free confirmed
- 📁 Files: none
- 🔁 Next prompts: user runs backend themselves; report browser test results
- 🧠 Reflection: only ONE owner for a dev server at a time - background + foreground instances caused all the port chaos

## Evaluation notes (flywheel)

- Failure modes observed: agent background instance conflicting with user terminal instance
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

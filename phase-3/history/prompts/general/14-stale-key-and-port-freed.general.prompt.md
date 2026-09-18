---
id: 14
title: Stale Key Confirmed Port Freed
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: diagnose-stale-key
labels: ["gemini", "api-key", "403", "port-conflict", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - Live Google API test with .env key: 403 PERMISSION_DENIED (key still old/blocked)
---

## Prompt

abe bhae gemini api key kbki update krde he abhi bhi backend start nhi horha he

## Response snapshot

Verified with a direct Google API call that backend/.env still contains the OLD blocked key (AIzaSyCirR5A..., .env modified 13:41 but same value) -> 403 PERMISSION_DENIED confirmed live. Explained: (1) backend WAS already running (PID 8968, my background instance) which is why the user's own start command hit errno 10048; (2) killed PID 8968 and freed port 8000 so the user's own start command will now work; (3) gave precise key-replacement steps - create key in a NEW project at aistudio.google.com/apikey, paste over the old GEMINI_API_KEY line in backend/.env, save, then start. Emphasized the full chain is already E2E-verified and only the key blocks live chat.

## Outcome

- ✅ Impact: Port freed for user's own startup; stale-key situation proven with live API evidence
- 🧪 Tests: live Google API check (403 PERMISSION_DENIED)
- 📁 Files: none (user must edit .env)
- 🔁 Next prompts: verify after user replaces key
- 🧠 Reflection: "key update kar di" vs file reality mismatch - always verify with a live call, not file mtime

## Evaluation notes (flywheel)

- Failure modes observed: user believed key was updated; file said otherwise
- Graders run and results (PASS/FAIL): 403 confirmed externally
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

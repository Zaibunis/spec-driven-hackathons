---
id: 22
title: Switch Primary Model Gemini 35 Flash
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: switch-model-35-flash
labels: ["gemini", "model-chain", "quota", "e2e-pass"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/chat/agent.py
tests:
 - Live chat on gemini-3.5-flash PASS
 - dashboard sync PASS
 - pytest 15/15
---

## Prompt

limit kkhatam hogye he 2.5 flash ki bhi ab 3.5 flash use kro

## Response snapshot

Updated GEMINI_MODEL_CHAIN per user request: gemini-3.5-flash is now primary (2.5-flash quota exhausted), gemini-3.5-flash-lite fallback, gemini-flash-latest last resort. Removed gemini-2.5-flash entirely. Restarted backend and verified live: signup -> chat 'Add a task called 35 flash check' -> AI confirmed 'I have successfully added the task 35 flash check' -> dashboard GET /v1/tasks shows it. pytest 15/15. (CRLF line endings required exact-match replace on Windows.)

## Outcome

- ✅ Impact: Chat back online on 3.5-flash with automatic fallback if quota hits again
- 🧪 Tests: live chat PASS, dashboard PASS, pytest 15/15
- 📁 Files: agent.py chain only
- 🔁 Next prompts: commit all fixes; optional history trimming for quota
- 🧠 Reflection: model chain makes model swaps a one-line change now

## Evaluation notes (flywheel)

- Failure modes observed: CRLF vs LF mismatch in str_replace - resolved via byte-level replace
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

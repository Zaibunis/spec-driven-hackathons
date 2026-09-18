---
id: 21
title: Quota Fix Model Fallback Chain
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: quota-model-fallback
labels: ["gemini", "quota", "429", "model-chain", "flash-lite", "e2e-pass"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/chat/agent.py
tests:
 - backend pytest (15 passed)
 - Live chat on new model chain PASS (task added + dashboard sync)
---

## Prompt

quota exceeded error now change the gemini model bcz i have already updated the gemini api key

## Response snapshot

Server log confirmed: 429 quota exceeded - free tier limit 5 RPM on gemini-2.5-flash (chat history burns requests fast since every turn re-sends context). Root fix: GEMINI_MODEL_CHAIN fallback in backend/src/chat/agent.py - primary gemini-3.5-flash-lite (Google's own 404 hint says 2.5-flash-lite retired for new users; first attempt at 2.5-flash-lite hit that 404, so moved to 3.5-flash-lite), then gemini-flash-latest, then gemini-2.5-flash. run_chat_agent refactored: outer loop catches 429/quota/RESOURCE_EXHAUSTED and falls to next model; inner _run_with_model holds the multi-round tool loop unchanged. Verified live: signup -> chat 'Add a task called Final model test' -> AI confirmed -> dashboard GET /v1/tasks shows the task. pytest 15/15.

## Outcome

- ✅ Impact: Quota 429 auto-recovers via model chain; chat resilient on free tier
- 🧪 Tests: pytest 15/15; live chat + dashboard sync PASS
- 📁 Files: agent.py (chain + refactor)
- 🔁 Next prompts: monitor 429 frequency; consider caching/trimming history to cut request count
- 🧠 Reflection: free tier 5 RPM is tiny for tool-loop chats; history replay multiplies request count - lite-tier models + fallback is the pragmatic fix

## Evaluation notes (flywheel)

- Failure modes observed: first chain entry (2.5-flash-lite) retired -> adapted to 3.5-flash-lite per Google's error hint
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

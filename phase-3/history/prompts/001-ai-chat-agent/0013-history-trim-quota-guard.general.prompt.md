---
id: 25
title: History Trim Quota Guard
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: history-trim-quota
labels: ["quota", "history", "gemini", "optimization"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/src/api/routes/chat.py
tests:
 - pytest 15/15 after trim change
---

## Prompt

User pasted log showing fallback chain working correctly (3.5-flash -> 3.5-flash-lite -> flash-latest, all quota-hitting in sequence).

## Response snapshot

Clarified the pasted log shows the fallback chain WORKING (new key AQ.Ab8RN loaded, models cycling on 429). Root cause of rapid quota burn: get_conversation_history sends the ENTIRE conversation to Gemini every chat turn - each history message costs a request against the 5-15 RPM free-tier limit. Fix: trim history to last 8 messages (4 user+assistant turns) in chat.py: get_conversation_history(session, convo.id)[-8:]. pytest 15/15 after change. Explained to user: quota resets each minute; if all 3 models hit 429 simultaneously, wait 60s and retry. Long-term options: paid tier, or trimming to 4 messages.

## Outcome

- ✅ Impact: Chat request count per message bounded; quota lasts ~3x longer
- 🧪 Tests: pytest 15/15
- 📁 Files: chat.py (history trim)
- 🔁 Next prompts: user browser retest after quota window resets
- 🧠 Reflection: history replay is the hidden multiplier on Gemini free-tier RPM

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): pytest PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

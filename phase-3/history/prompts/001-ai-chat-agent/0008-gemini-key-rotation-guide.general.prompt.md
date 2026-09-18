---
id: 9
title: Gemini 403 Key Rotation Guide
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: debug-gemini-403
labels: ["gemini", "api-key", "403", "configuration", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files: []
tests:
 - backend key prefix check (AIzaSyCirR = old blocked key still in .env)
---

## Prompt

Error: 403 Your project has been denied access. Please contact support. (thrown in ChatKitWrapper.tsx:55 handleSendMessage)

## Response snapshot

Verified .env still holds the old blocked Gemini key (prefix AIzaSyCirR). The 403 is Google-side (project denied); frontend error propagation via body.detail is working as designed. Guided user: create new API key in a NEW project at aistudio.google.com/apikey, replace GEMINI_API_KEY in backend/.env, restart uvicorn (taskkill //F //IM python.exe caution noted), then retest chat -> MCP add task -> dashboard live sync. Fallback if new key also 403: different Google account or Google support.

## Outcome

- ✅ Impact: Clear unblock path for user; no code changes needed
- 🧪 Tests: key prefix verification done
- 📁 Files: none (user edits .env)
- 🔁 Next prompts: full E2E test after new key
- 🧠 Reflection: Correct error surfacing proves new chat->backend wiring works end to end

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

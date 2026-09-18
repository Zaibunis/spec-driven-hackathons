---
id: 8
title: Chat Dashboard Task Sync Fix
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: 001-ai-chat-agent
branch: main
user: unknown
command: fix-chat-dashboard-sync
labels: ["frontend", "chat", "dashboard", "tasks", "sync", "debugging"]
links:
  spec: specs/001-ai-chat-agent
  ticket: null
  adr: null
  pr: null
files:
 - frontend/src/app/(dashboard)/tasks/page.tsx
 - frontend/src/components/ChatInterface/ChatKitWrapper.tsx
tests:
 - frontend tsc --noEmit (clean)
---

## Prompt

if the chat says task added but why it does not shows on my task dashboard? (Roman Urdu preferred; local backend, not HF)

## Response snapshot

Root cause: 3 frontend bugs. (1) ChatKitWrapper bypassed backend entirely - called Gemini API directly from browser with no JWT and no MCP tools, so "task added" was model text with zero DB writes (verified: task table had 0 rows). Rewired to POST {NEXT_PUBLIC_API_URL}/api/v1/{userId}/chat with Bearer token, parsing assistant_message. (2) Dashboard tasks page was a stub - loadTasks did setTasks([]) with "In a real implementation" comment. Replaced with real GET /v1/tasks fetch (Bearer token), mapping snake_case fields (is_completed/created_at) to the frontend Task shape; add/update/toggle/delete wired to POST/PUT/PATCH/DELETE /v1/tasks (toggle uses PATCH per backend routes; list returns {tasks:[...]}). (3) No refresh path from chat to dashboard - added window CustomEvent 'todo:tasks-changed' dispatched by chat after each assistant reply, listened on tasks page to refetch. tsc --noEmit clean. Chat responses still blocked externally by the 403 project-denied Gemini key until user creates a new one.

## Outcome

- ✅ Impact: Chat MCP operations and dashboard now share the same backend source of truth; dashboard live-refreshes after chat actions
- 🧪 Tests: tsc clean; E2E pending new Gemini key
- 📁 Files: tasks/page.tsx (real API), ChatKitWrapper.tsx (backend chat + event)
- 🔁 Next prompts: add new Gemini key and E2E test; consider TaskContext/jotai for state dedup
- 🧠 Reflection: Frontend had a parallel "direct-to-Gemini" chat path with no tools - the classic cause of "AI said it, DB disagrees"

## Evaluation notes (flywheel)

- Failure modes observed: mock stubs left in shipped pages
- Graders run and results (PASS/FAIL): tsc PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

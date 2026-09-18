---
id: 38
title: Failed To Fetch Trailing Slash CORS
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "Console TypeError: Failed to fetch at loadTasks (src/app/(dashboard)/tasks/page.tsx:42:25) - fetch(`${apiUrl}/v1/tasks`)"
labels: ["cors", "frontend", "trailing-slash", "fetch", "vercel"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - frontend/src/lib/api-url.ts (created - shared getApiBaseUrl helper)
  - frontend/src/app/(dashboard)/tasks/page.tsx
  - frontend/src/components/ChatInterface/ChatKitWrapper.tsx
  - frontend/src/services/api-client.ts
  - frontend/src/lib/api-client.ts
  - frontend/src/lib/auth.ts
tests_yaml: |
  - npx tsc --noEmit (pass, exit 0)
  - CORS preflight OPTIONS /v1/tasks from localhost:3000 (200 with proper ACAO headers)
  - double-slash URL test //v1/tasks -> 308 without CORS headers (reproduced root cause)
prompt_text: |
  ## Error TypeConsole TypeError## Error MessageFailed to fetch    at loadTasks (src/app/(dashboard)/tasks/page.tsx:42:25)    at TasksPage.useEffect (src/app/(dashboard)/tasks/page.tsx:18:7)## Code Frame  40 |  41 |       const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'https://hackathon-phase-4-eight.vercel.app/';> 42 |       const res = await fetch(`${apiUrl}/v1/tasks`, {     |                         ^  43 |         headers: { Authorization: `Bearer ${token}` },  44 |       });  45 |Next.js version: 16.1.1 (Turbopack)
response_text: |
  Diagnosed via curl: backend healthy, CORS preflight passes, but .env.local
  NEXT_PUBLIC_API_URL ends with a trailing slash -> request URL becomes
  //v1/tasks -> 308 redirect without CORS headers -> browser blocks with
  "Failed to fetch". Fix (9cd4f24): added shared getApiBaseUrl() that strips
  trailing slashes, wired into all 5 API call sites (tasks page, chat wrapper,
  both axios clients, better-auth client). Also removed stale HF Space
  fallbacks. tsc clean.
outcome: success
---

# PHR 38 — Failed To Fetch Trailing Slash CORS

## User prompt (verbatim)
Console TypeError: Failed to fetch at loadTasks (src/app/(dashboard)/tasks/page.tsx:42:25) at TasksPage.useEffect (src/app/(dashboard)/tasks/page.tsx:18:7). Code frame showed apiUrl default 'https://hackathon-phase-4-eight.vercel.app/' (trailing slash).

## Response summary
- Root cause reproduced with curl: trailing slash -> //v1/tasks -> 308 redirect WITHOUT CORS headers -> browser "Failed to fetch".
- Fix: shared getApiBaseUrl() strips trailing slashes; used in all 5 call sites; removed stale hf.space fallbacks (9cd4f24).
- Backend CORS preflight verified passing; backend healthy.
- Next: frontend redeploy, then set FRONTEND_ORIGINS on backend to frontend production URL + redeploy backend.

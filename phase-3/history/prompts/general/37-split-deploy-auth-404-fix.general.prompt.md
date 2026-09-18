---
id: 42
title: Split Deploy Auth 404 Fix
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "menee dono backend and frontend alag deploy kre hen or jb frontend deploy krdy alag to usme signin or signup krrhe the to not found arah he"
labels: ["vercel", "auth", "404", "split-deployment", "frontend"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - frontend/src/lib/api-url.ts (fallback now = deployed backend URL, never self-origin)
  - frontend/src/lib/api-client.ts (removed window.location.origin + /api/v1 fallback logic)
  - frontend/src/lib/auth.ts (removed stale hf.space / window-origin fallbacks)
tests_yaml: |
  - live curl: POST /auth/auth/signin -> 401 INVALID_CREDENTIALS (route exists, backend OK)
  - live curl: POST /auth/auth/signup -> 201 with token (backend auth fully working)
  - openapi.json: /auth/auth/signin and /auth/auth/signup present
  - npx tsc --noEmit (pass)
prompt_text: |
  menee dono backend and frontend alag deploy kre hen or jb frontend deploy krdy alag to usme signin or signup krrhe the to not found arah he
response_text: |
  Backend verified healthy (signin 401/invalid creds, signup 201 with token). 404 came
  from frontend: axios + better-auth clients fell back to window.location.origin(+/api/v1)
  when NEXT_PUBLIC_API_URL was unset, hitting the frontend's own domain (no API there).
  Fix 6e760a6: single getApiBaseUrl() with fallback = https://hackathon-phase-4-eight.vercel.app;
  removed all self-origin/hf.space/api-v1 rewrite logic. Backend CORS already includes
  hackathon-phase-4-afqe.vercel.app (a157add). Next: redeploy frontend so new build inlines
  correct URL.
outcome: success
---

# PHR 42 — Split Deploy Auth 404 Fix

## User prompt (verbatim)
menee dono backend and frontend alag deploy kre hen or jb frontend deploy krdy alag to usme signin or signup krrhe the to not found arah he

## Response summary
- Backend auth routes verified live and working (signin 401, signup 201).
- Root cause: frontend clients self-origin fallback when NEXT_PUBLIC_API_URL unset -> requests hit frontend domain -> Vercel 404.
- Fix (6e760a6): getApiBaseUrl() fallback = deployed backend; removed stale rewrite logic from axios + better-auth clients.
- Reminder: NEXT_PUBLIC_ vars inline at build time - env changes need redeploy.

---
id: 36
title: Vercel 404 Rewrite Path Fix
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "detail not found [pasted runtime logs showing GET 404 on /api/index, / plus earlier 'Database initialized successfully' and ModuleNotFoundError history]"
labels: ["vercel", "404", "routing", "rewrites", "fastapi"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/vercel.json (removed rewrites, keyed functions on src/main.py)
tests_yaml: |
  - pending: /health check after auto-deploy of 4328b95
prompt_text: |
  detail not found [pasted Vercel runtime logs]
response_text: |
  Logs showed "Database initialized successfully" - app imports and boots fine now
  (deps fix worked, bundle OK). Remaining 404s are routing: backend framework mode
  routes by rewritten destination path, and our /(.) rewrite made the app receive
  /api/index, which has no FastAPI route. Fix (4328b95): removed rewrites entirely
  and keyed functions on the resolved entrypoint src/main.py with includeFiles
  src/** and maxDuration 60. Vercel now passes original paths (/health, /v1/tasks)
  straight to the app. Pending: verify /health after auto-deploy.
outcome: success
---

# PHR 36 — Vercel 404 Rewrite Path Fix

## User prompt (verbatim)
detail not found [pasted Vercel runtime logs: 404s on /api/index, /; earlier 500 ModuleNotFoundError; "Database initialized successfully" line present]

## Response summary
- Key insight: app now boots on Vercel ("Database initialized successfully") — dependency fix worked.
- 404 root cause: /(.) rewrite made app see rewritten path /api/index (no such route) due to new backend-framework routing behavior.
- Fix (4328b95): removed rewrites; functions keyed on src/main.py (framework entrypoint).
- Next: test /health and /docs after auto-deploy; then wire frontend NEXT_PUBLIC_API_URL + FRONTEND_ORIGINS.

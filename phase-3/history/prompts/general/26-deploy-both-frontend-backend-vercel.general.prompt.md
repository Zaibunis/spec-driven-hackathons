---
id: 31
title: Deploy Frontend Backend Together Vercel
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "dono ek sath deploy krdun frontend and backend?"
labels: ["vercel", "deployment", "cors", "nextjs", "fastapi"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/src/main.py (modified - FRONTEND_ORIGINS env var for CORS)
tests_yaml: |
  - python -m py_compile backend/src/main.py (pass)
prompt_text: |
  dono ek sath deploy krdun frontend and backend?
response_text: |
  Advised two separate Vercel projects from the same repo (one with root=backend, one with
  root=frontend) rather than mixing runtimes in one project. Made CORS configurable via
  FRONTEND_ORIGINS env var (comma-separated) in backend/src/main.py so deployed frontend URL
  can be added without code change. Committed 37a1d40 and pushed. Deployment order: backend
  project first (get URL) -> frontend env NEXT_PUBLIC_API_URL=<backend-url> and backend env
  FRONTEND_ORIGINS=<frontend-url> -> test /health -> full chat+dashboard E2E.
outcome: success
---

# PHR 31 — Deploy Frontend Backend Together Vercel

## User prompt (verbatim)
dono ek sath deploy krdun frontend and backend?

## Response summary
- Yes: two separate Vercel projects from same repo (root=backend and root=frontend).
- Added `FRONTEND_ORIGINS` env var support in backend CORS (no redeploys needed to change origins).
- Commit `37a1d40` pushed to origin/main.
- Order: deploy backend first → copy URL → set NEXT_PUBLIC_API_URL on frontend project → set FRONTEND_ORIGINS on backend project → verify /health → E2E chat+dashboard.

---
id: 29
title: Vercel Backend Deploy Setup
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "backend bhi vercel pr krun ?"
labels: ["vercel", "deployment", "fastapi", "serverless"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/api/index.py (created - Vercel Python serverless entrypoint)
  - backend/vercel.json (created - rewrites + maxDuration 60)
tests_yaml: |
  - python -m py_compile backend/api/index.py (pass)
prompt_text: |
  backend bhi vercel pr krun ?
response_text: |
  Answered yes with caveats. Created backend/api/index.py (sys.path fix + imports src.main.app) and
  backend/vercel.json (rewrite all paths to /api/index, maxDuration 60s for chat). Deploy steps:
  Vercel project with root=backend, framework=Other, env vars DATABASE_URL/JWT_SECRET/
  BETTER_AUTH_SECRET/GEMINI_API_KEY, then set frontend NEXT_PUBLIC_API_URL to the Vercel URL.
  Caveats documented: serverless cold starts (first chat request slow), lifespan init_db skipped
  (tables already exist on Neon), CORS must include the frontend Vercel URL in src/main.py.
outcome: success
---

# PHR 29 — Vercel Backend Deploy Setup

## User prompt (verbatim)
backend bhi vercel pr krun ?

## Response summary
- Confirmed Vercel can host FastAPI via its Python serverless runtime.
- Created `backend/api/index.py` (entrypoint: sys.path insert backend root, `from src.main import app`).
- Created `backend/vercel.json` (catch-all rewrite to `/api/index`, `maxDuration: 60`).
- Deploy flow: Vercel → New Project → repo → root `backend` → framework Other → env vars (DATABASE_URL, JWT_SECRET, BETTER_AUTH_SECRET, GEMINI_API_KEY) → deploy.
- Frontend wiring: set `NEXT_PUBLIC_API_URL` to the backend Vercel URL; add frontend URL to CORS in `backend/src/main.py`.
- Caveats: serverless cold starts; init_db runs at function init (tables already exist on Neon so it is skipped); chat max 60s per request.

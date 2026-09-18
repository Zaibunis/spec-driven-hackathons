---
id: 35
title: Vercel Bundle Size Limit Slim Deps
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "WARNING! Internal rewrites in backend framework projects now route requests using the rewritten destination path... Error: Total bundle size (236.81 MB) exceeds the maximum function size (225 MB)."
labels: ["vercel", "deployment", "bundle-size", "requirements"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/requirements.txt (runtime-only deps)
  - backend/requirements-dev.txt (created - dev/local extras)
tests_yaml: |
  - grep audit of src imports (uvicorn/alembic/pytest/httpx/multipart unused at runtime)
prompt_text: |
  WARNING! Internal rewrites in backend framework projects now route requests using the rewritten destination path. This behavior was previously unsupported and may change which application route handles a request. Review your rewrite configuration to ensure this behavior is expected.Error: Total bundle size (236.81 MB) exceeds the maximum function size (225 MB).
response_text: |
  installCommand fix (114ca0e) worked - pip install ran, bundle grew past 225 MB because
  heavy non-runtime packages (uvicorn[standard], pytest, pytest-asyncio, httpx, alembic,
  python-multipart) were in requirements.txt. Grepped src/ for imports: none of those are
  imported at runtime (uvicorn only in local __main__ block). Moved dev deps to new
  requirements-dev.txt; runtime file keeps fastapi, pydantic(-settings), sqlmodel,
  psycopg2-binary, asyncpg, google-generativeai, python-dotenv, bcrypt, pyjwt,
  python-jose, passlib. Committed dce65d4 and pushed - Vercel auto-deploys.
outcome: success
---

# PHR 35 — Vercel Bundle Size Limit Slim Deps

## User prompt (verbatim)
WARNING! Internal rewrites in backend framework projects now route requests using the rewritten destination path. This behavior was previously unsupported and may change which application route handles a request. Review your rewrite configuration to ensure this behavior is expected.Error: Total bundle size (236.81 MB) exceeds the maximum function size (225 MB).

## Response summary
- Progress: pip install now RUNS on Vercel (installCommand fix worked).
- New error: bundle 236.81 MB > 225 MB limit.
- Root cause: dev/test/local packages bundled via requirements.txt.
- Fix: runtime-only requirements.txt + new requirements-dev.txt (commit dce65d4).
- Next: verify auto-deploy build succeeds and /health returns healthy.

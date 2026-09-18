---
id: 33
title: Vercel Backend Env Var Checklist
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: ".env me kya kya dalon backend ke vercel me"
labels: ["vercel", "env-vars", "deployment", "configuration"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/src/config.py (read - required vs optional settings)
tests_yaml: |
  - none
prompt_text: |
  .env me kya kya dalon backend ke vercel me
response_text: |
  Verified backend/src/config.py: only database_url and jwt_secret are mandatory; all others have
  defaults. Vercel env list: required DATABASE_URL, JWT_SECRET; recommended BETTER_AUTH_SECRET,
  GEMINI_API_KEY (read via os.environ in agent.py - works on Vercel since load_dotenv is a no-op
  without a .env file), FRONTEND_ORIGINS (after frontend deploy + one redeploy). Optional demo
  convenience: JWT_EXPIRATION_MINUTES=60 (default 15 causes frequent 401/signin redirects).
  Skip: API_HOST/API_PORT (serverless ignores), JWT_ALGORITHM, BCRYPT_ROUNDS, DEBUG, LOG_LEVEL.
outcome: success
---

# PHR 33 — Vercel Backend Env Var Checklist

## User prompt (verbatim)
.env me kya kya dalon backend ke vercel me

## Response summary
- Required: DATABASE_URL, JWT_SECRET (config.py mandatory fields).
- Recommended: BETTER_AUTH_SECRET, GEMINI_API_KEY, FRONTEND_ORIGINS (post-frontend-deploy).
- Optional: JWT_EXPIRATION_MINUTES=60 for demo convenience.
- Skip: API_HOST, API_PORT, JWT_ALGORITHM, BCRYPT_ROUNDS, DEBUG, LOG_LEVEL (defaults fine).
- GEMINI_API_KEY works on Vercel: agent.py falls back to os.environ when no .env file exists.

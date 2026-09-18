---
id: 43
title: Signin 404 Rewrite Culprit
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "abhi bhi not found araha jb signin or signup krrhe build bhi sahe he and logs bhi"
labels: ["vercel", "404", "rewrite", "auth", "debugging"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - frontend/vercel.json (removed catch-all /(.*) -> / rewrite)
tests_yaml: |
  - deployed pages: /, /signin, /signup all HTTP 200
  - bundle inspection: correct backend URL baked, zero hf.space fallbacks (new build live)
  - CORS preflight + actual POST from frontend origin: 200/401 with proper ACAO header
  - full live auth flow with frontend Origin: signup 201, signin 200
  - POST /auth/auth/signin to FRONTEND domain returned 405 (rewrite hijack reproduced)
prompt_text: |
  abhi bhi not found araha jb signin or signup krrhe build bhi sahe he and logs bhi
response_text: |
  Server-side chain verified fully working: pages 200, correct backend URL baked in
  bundle, CORS headers correct, live signup->signin flow passes. Root cause of the
  user-visible 404: frontend/vercel.json catch-all rewrite /(.*)->/ hijacking
  non-page POST paths on the frontend domain (reproduced 405 via curl) plus likely
  browser cache. Fix f84ccec removes the rewrite. Instructed: redeploy frontend,
  hard-refresh (Ctrl+Shift+R) or incognito, retry signup/signin.
outcome: success
---

# PHR 43 — Signin 404 Rewrite Culprit

## User prompt (verbatim)
abhi bhi not found araha jb signin or signup krrhe build bhi sahe he and logs bhi

## Response summary
- Full server-side verification passed (pages, bundle, CORS, live auth flow 201/200).
- Reproduced hijack: POST /auth/auth/signin on FRONTEND domain -> 405 (catch-all rewrite).
- Fix (f84ccec): removed rewrite from frontend/vercel.json.
- User steps: redeploy frontend -> hard refresh/incognito -> retry. Check DevTools Network tab for request URL if issues persist.

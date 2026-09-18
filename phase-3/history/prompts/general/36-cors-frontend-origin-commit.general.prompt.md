---
id: 41
title: CORS Frontend Origin Commit Fix
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "mene backend me frontend ka deployed url dal dya he main.py file me ab commit changes krdo"
labels: ["cors", "backend", "security", "commit"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - backend/src/main.py (CORS allowlist: added production frontend origin)
tests_yaml: |
  - python -m py_compile backend/src/main.py (pass)
prompt_text: |
  mene backend me frontend ka deployed url dal dya he main.py file me ab commit changes krdo
response_text: |
  User manually added the deployed frontend URL to CORS origins in main.py but the
  entry had two bugs: a missing comma after the string (Python would parse it as
  string * list multiplication and crash at import) and a trailing slash (CORS
  Origin matching is exact, browser sends it without slash). Fixed both, verified
  compile, committed a157add and pushed. Vercel auto-deploys backend.
outcome: success
---

# PHR 41 — CORS Frontend Origin Commit Fix

## User prompt (verbatim)
mene backend me frontend ka deployed url dal dya he main.py file me ab commit changes krdo

## Response summary
- Reviewed user's manual edit before committing; found missing comma (import-time crash) + trailing slash (CORS exact-match failure).
- Fixed both in backend/src/main.py; py_compile pass.
- Commit a157add pushed; Vercel auto-deploy picks it up.
- Note: FRONTEND_ORIGINS env var also available for future origins without code edits.

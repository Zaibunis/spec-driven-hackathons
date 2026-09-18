---
id: 44
title: Trailing Space URL Baked 404
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "Failed to load resource 404 - 931d1e8593fc62a9.js Sign in error: AxiosError 404 (chunk 931d1e8593fc62a9 was the current deployed build)"
labels: ["404", "env-var", "trailing-space", "axios", "vercel"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - frontend/src/lib/api-url.ts (trim() before slash-strip)
  - frontend/.env.local (cleaned NEXT_PUBLIC_API_URL, verified with cat -A)
tests_yaml: |
  - bundle byte inspection: baked value was "https://hackathon-phase-4-eight.vercel.app/ " (slash+space)
  - cat -A verification of fixed local .env.local (clean line ending)
  - npx tsc --noEmit (pass)
prompt_text: |
  Failed to load resource: the server responded with a status of 404 () 931d1e8593fc62a9.js:1 Sign in error: AxiosError: Request failed with status code 404 ...
response_text: |
  User's error named the exact chunk previously analyzed - so the live build WAS current
  and the earlier rewrite fix was not the culprit. Byte-level bundle grep revealed the
  real root cause: Vercel env var NEXT_PUBLIC_API_URL was pasted as
  "https://hackathon-phase-4-eight.vercel.app/ " (trailing slash + SPACE). The slash-strip
  regex never ran because the string ended in whitespace, so requests became
  /%20//auth/auth/signin -> 404. Fix 312c3bb: trim() then strip slashes in getApiBaseUrl().
  Also cleaned local .env.local. User must fix the Vercel env var value and redeploy.
outcome: success
---

# PHR 44 — Trailing Space URL Baked 404

## User prompt (verbatim)
Failed to load resource: the server responded with a status of 404 ()931d1e8593fc62a9.js:1 Sign in error: AxiosError: Request failed with status code 404 at eC ... at async Object.signIn ...

## Response summary
- Chunk ID proved live build was current (not a cache issue).
- Byte-level bundle inspection: env var value ended in "/ " (slash+space) -> strip regex no-op -> %20 in request path -> 404.
- Fix (312c3bb): .trim() before slash-strip in getApiBaseUrl(); local .env.local cleaned (cat -A verified).
- User action: correct Vercel frontend env var value (no trailing slash/space) and redeploy.

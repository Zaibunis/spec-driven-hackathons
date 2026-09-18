---
id: 32
title: Confirm Both Projects On Vercel
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "backend and frontend dono vercel pr deploy krun?"
labels: ["vercel", "deployment", "confirmation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - none (no code changes)
tests_yaml: |
  - none
prompt_text: |
  backend and frontend dono vercel pr deploy krun?
response_text: |
  Confirmed: deploy both on Vercel as two separate projects from the same repo (root=backend and
  root=frontend). Order: backend first (copy URL, test /health), then frontend with
  NEXT_PUBLIC_API_URL set, finally FRONTEND_ORIGINS on backend + one redeploy. Noted free-tier
  caveats: 2-5s serverless cold start on first request; per-root auto-deploys handled by Vercel.
outcome: success
---

# PHR 32 — Confirm Both Projects On Vercel

## User prompt (verbatim)
backend and frontend dono vercel pr deploy krun?

## Response summary
- Confirmed both-on-Vercel as the simplest setup; two separate projects from one repo.
- Deploy order: backend → copy URL → frontend (NEXT_PUBLIC_API_URL) → FRONTEND_ORIGINS + redeploy.
- Caveats repeated: serverless cold start (2-5s), auto-redeploy per push scoped by root directory.

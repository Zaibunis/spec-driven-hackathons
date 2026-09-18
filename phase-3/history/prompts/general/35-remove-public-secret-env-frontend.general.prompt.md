---
id: 40
title: Remove Public Secret Env Frontend
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "next public gemini api kiu likha ye public thore he secret he in frontend .env.local / isko next public hata do bs gemini api key likho or jaha use hue he waha updte krdo"
labels: ["security", "env-vars", "frontend", "secrets", "nextjs"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - frontend/.env.local (removed 4 dead vars incl. NEXT_PUBLIC_GEMINI_API_KEY; backup .env.local.bak gitignored)
  - frontend/.env.example (removed public-secret placeholders, added security docs)
tests_yaml: |
  - grep frontend/ for GEMINI_API_KEY|BETTER_AUTH_SECRET|DATABASE_URL|NEXT_PUBLIC_DEBUG -> 0 code references (all dead)
  - git log --all -- .env.local -> never committed
  - git check-ignore .env.local.bak -> ignored
prompt_text: |
  next public gemini api kiu likha ye public thore he secret he in frontend .env.local
  isko next public hata do bs gemini api key likho or jaha use hue he waha updte krdo
response_text: |
  User correctly flagged NEXT_PUBLIC_ secret exposure. Audit found the key was never
  referenced anywhere in frontend code (0 matches) - all Gemini calls happen in the
  backend, which already uses plain GEMINI_API_KEY. Removed 4 dead vars from
  frontend/.env.local (NEXT_PUBLIC_GEMINI_API_KEY, NEXT_PUBLIC_BETTER_AUTH_SECRET,
  DATABASE_URL, NEXT_PUBLIC_DEBUG); only NEXT_PUBLIC_API_URL remains. Cleaned
  frontend/.env.example with security documentation (commit c71c6c6). Key was never
  in a bundle (unreferenced NEXT_PUBLIC_ vars are not inlined) and never committed,
  so no rotation required.
outcome: success
---

# PHR 40 — Remove Public Secret Env Frontend

## User prompt (verbatim)
next public gemini api kiu likha ye public thore he secret he in frontend .env.local
isko next public hata do bs gemini api key likho or jaha use hue he waha updte krdo

## Response summary
- Principle confirmed: NEXT_PUBLIC_ vars are public (baked into browser bundle).
- Audit: frontend code never used the Gemini key - backend owns it as GEMINI_API_KEY already.
- Removed 4 dead vars from .env.local; only NEXT_PUBLIC_API_URL remains.
- frontend/.env.example cleaned with security note (c71c6c6, pushed).
- Exposure risk: none (never referenced -> never inlined; never committed).

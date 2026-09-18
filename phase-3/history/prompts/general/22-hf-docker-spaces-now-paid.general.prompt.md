---
id: 27
title: HF Docker Spaces Now Paid
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "hugging face me docker option paid hogya now?"
labels: ["hugging-face", "pricing", "deployment", "render", "koyeb"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - deploy/hf-backend/Dockerfile (reusable on Render/Koyeb)
tests_yaml: |
  - none
prompt_text: |
  hugging face me docker option paid hogya now?
response_text: |
  Confirmed via HF docs + community forum (July 2026): Gradio and Docker Spaces now require a paid
  plan (PRO for personal accounts, Team/Enterprise for orgs); only Static Spaces remain free.
  Recommended free alternatives: Render free web service (Docker runtime, 5GB bandwidth, 15-min
  spin-down, cold starts) or Koyeb free web service (512MB RAM, 0.1 vCPU, one free service).
  deploy/hf-backend/Dockerfile works as-is (just needs $PORT env var adjustment). Path A
  (Minikube+Helm local) is unaffected by this change.
outcome: success
---

# PHR 27 — HF Docker Spaces Now Paid

## User prompt (verbatim)
hugging face me docker option paid hogya now?

## Response summary
- Confirmed: HF Docker/Gradio Spaces are paid-only since July 2026 (PRO $9/mo for personal, Team/Enterprise for orgs); Static Spaces remain free.
- Existing Space URL from earlier deployment is dead; do not rely on it.
- Best free alternatives: Render (free web service, Docker runtime) or Koyeb (free web service, 512MB).
- deploy/hf-backend/Dockerfile reusable — minor PORT env tweak needed for Render/Koyeb.
- Minikube+Helm local path unaffected.

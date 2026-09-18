---
id: 6
title: Redeploy Backend On Hugging Face
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: deployment-guidance
labels: ["backend", "hugging-face", "deployment", "docker", "runbook"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - deploy/hf-backend/Dockerfile
 - deploy/hf-backend/README.md
tests: []
---

## Prompt

the backend is deployed on hugging face how to access that on hugging face bcz when i open my account there is no space of it so i am thinking to again deploy my backend give me steps

## Response snapshot

Old Space (faria45678-chat-agent.hf.space, still hardcoded as fallback in frontend/src/lib/auth.ts) no longer exists in the user's account. Created deploy/hf-backend/Dockerfile (python:3.11-slim, uid 1000, port 7860, uvicorn src.main:app) and deploy/hf-backend/README.md (HF Space front-matter: sdk docker, app_port 7860). Provided 4-step runbook: (1) create Docker Space, (2) upload both files, (3) set Space secrets DATABASE_URL/JWT_SECRET/BETTER_AUTH_SECRET/GEMINI_API_KEY - rotate Neon password first since it was leaked, (4) point frontend NEXT_PUBLIC_API_URL at new space URL. Flagged CORS: backend allowlist covers localhost:3000 and phase-3-six.vercel.app only; other frontend origins need main.py update. Alternative git-push flow documented. Noted free-tier 48h sleep + cold start.

## Outcome

- ✅ Impact: Reproducible backend redeployment; secrets stay out of image via Space secrets
- 🧪 Tests: none yet - pending user executing deployment
- 📁 Files: deploy/hf-backend/{Dockerfile,README.md}
- 🔁 Next prompts: add new space URL to CORS; update frontend env; verify /health remotely
- 🧠 Reflection: HF Spaces need app_port 7860 and uid 1000; secrets must never be baked into image (consistent with GitRoll remediation policy)

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none

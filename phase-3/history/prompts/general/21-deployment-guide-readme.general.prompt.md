---
id: 21
title: Deployment Guide From READMEs
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: ZAINAB KHAN
command: "now how to deploy everything works perfectly read all the readme"
labels: ["deployment", "minikube", "helm", "hugging-face", "vercel", "docker"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - README.md (read)
  - backend/README.md (read)
  - frontend/README.md (read)
  - deploy/hf-backend/README.md (read)
  - chatbot.md (read)
  - docker-compose.yml (read)
  - k8s/charts/todo-app/values.yaml (read)
tests_yaml: |
  - none
prompt_text: |
  now how to deploy everything works perfectly read all the readme
response_text: |
  Read all READMEs (root Phase-IV Minikube+Helm, backend, frontend, deploy/hf-backend HF Space,
  chatbot.md) plus docker-compose.yml, Helm values, Dockerfiles, env examples. Verified toolchain:
  Docker/Minikube/Helm/kubectl not installed on this machine. Presented two deploy paths:
  (A) Minikube+Helm local K8s per README with full command sequence (tools install, minikube start,
  eval docker-env, build images, create namespace/secret, helm install, minikube service), noting
  frontend NEXT_PUBLIC_API_URL must be the backend service URL and Helm existingSecret is
  todo-backend-secrets. (B) Cloud path: backend as HF Docker Space (deploy/hf-backend Dockerfile,
  Space secrets DATABASE_URL/JWT_SECRET/BETTER_AUTH_SECRET/GEMINI_API_KEY, rotate Neon password),
  frontend on Vercel with NEXT_PUBLIC_API_URL set; warned about stale hardcoded HF URL fallback in
  frontend/src/lib/api-client.ts and auth.ts and CORS allowlist update in backend main.py.
outcome: success
---

# PHR 21 — Deployment Guide From READMEs

## User prompt (verbatim)
now how to deploy everything works perfectly read all the readme

## Response summary
- Discovered deploy assets: `deploy/hf-backend/` (Dockerfile + README for HF Space), `k8s/charts/todo-app/` (Helm chart, existingSecret=todo-backend-secrets), root `todo-*-deployment.yaml` (raw manifests), `docker-compose.yml` (fail-fast on missing env, no baked secrets).
- Verified Docker/Minikube/Helm/kubectl are NOT installed locally → path A requires tool installation first.
- Path A (Minikube+Helm, README Phase-IV): install tools → minikube start → eval $(minikube docker-env) → docker build both images → kubectl create namespace todo-app + secret todo-backend-secrets → helm install todo-chatbot-release ./k8s/charts/todo-app → minikube service todo-app-frontend.
- Path B (cloud): HF Docker Space from deploy/hf-backend (secrets in Space settings, rotate Neon password) + Vercel frontend with NEXT_PUBLIC_API_URL; fix stale fallback URL in api-client.ts/auth.ts and backend CORS.

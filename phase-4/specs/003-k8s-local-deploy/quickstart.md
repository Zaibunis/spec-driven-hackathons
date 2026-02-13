# Quickstart Guide: Phase 4 Local Kubernetes Deployment

**Feature**: Local Kubernetes Deployment (Minikube)  
**Date**: 2026-02-13  
**Branch**: 003-local-k8s-deploy

## Overview

This guide provides essential steps to deploy the Phase-3 AI Chatbot application to a local Minikube cluster using Helm. The setup includes building Docker images locally, configuring secrets, and accessing frontend and backend services.

---

## Prerequisites

- Docker Desktop (running)
- Minikube installed
- Helm installed
- kubectl installed
- Your terminal pointing to Minikube’s Docker daemon

---

## 1. Start Minikube

Start Minikube and configure your shell to use Minikube’s Docker daemon. This allows images to be built directly in Minikube.

```bash
# Start Minikube
minikube start

# Powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

# Bash
eval $(minikube -p minikube docker-env)
2. Build Docker Images
Build the frontend and backend images using your preferred tags:

# Frontend
cd frontend
docker build -t todo-frontend .

# Backend
cd ../backend
docker build -t todo-backend .
Note: Ensure the images are available in Minikube’s Docker daemon by running docker images.

3. Configure Secrets
Create a local secrets file (DO NOT COMMIT) for environment variables:

my-secrets.yaml

secrets:
  databaseUrl: "postgresql://username:password@host:port/dbname"
  openaiApiKey: "sk-..."
  geminiApiKey: "..."
  betterAuthSecret: "your-secret-key"
Required Environment Variables

Backend (backend/.env)

DATABASE_URL – Neon PostgreSQL connection string

BETTER_AUTH_SECRET – Secret for JWT auth

GEMINI_API_KEY – API key for Gemini

GEMINI_BASE_URL – (Optional) Custom Gemini base URL

CORS_ORIGINS – Comma-separated allowed origins

Frontend (frontend/.env)

NEXT_PUBLIC_API_URL – Backend API URL

BETTER_AUTH_SECRET – Must match backend

BETTER_AUTH_URL – Frontend application URL
```

4. Deploy via Helm
Navigate to the Helm chart directory and install the application:

cd ../deploy/helm
helm install todo-app ./todo-chatbot -f ../../my-secrets.yaml
5. Access the Application
Get the frontend and backend service URLs:

# Frontend
minikube service todo-app-frontend --url

# Backend
minikube service todo-app-backend --url
Open the frontend URL in your browser to interact with the AI Chatbot.

6. AIOps Tools (Optional)
kubectl-ai – Run natural language queries for cluster operations:

# Scale frontend
kubectl-ai "Scale the frontend deployment to 3 replicas"

# Troubleshoot backend pod
kubectl-ai "Why is the backend pod in CrashLoopBackOff?"

# List services
kubectl-ai "List all services in the todo-chatbot namespace"
kagent – Intelligent cluster analysis:

# Analyze cluster health
kagent analyze --namespace todo-chatbot

# Optimize resources for backend
kagent recommend --deployment todo-backend
Troubleshooting
ImagePullBackOff: Ensure you ran docker-env before building images.

CrashLoopBackOff: Check logs with kubectl logs <pod-name>; usually missing environment variables.

Database Connection Errors: Verify Neon DB URL and network access from Minikube.

Notes
The build commands in this setup are:

docker build -t todo-frontend .
docker build -t todo-backend .
Access services with:

minikube service todo-app-frontend
minikube service todo-app-backend
Verify all environment variables are properly configured in secrets for successful deployment.
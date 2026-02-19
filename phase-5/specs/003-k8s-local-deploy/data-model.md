# Data Model: Phase 4 Local Kubernetes Deployment

**Feature Branch**: 003-local-k8s-deploy  
**Date**: 2026-02-13  

This document defines the infrastructure data model for deploying the Phase-3 AI Chatbot application to a local Minikube cluster using Helm. It outlines Kubernetes resources, configuration, and Helm values structure.

---

## 1. Kubernetes Resources

### 1.1 Deployments

**frontend-deployment**
- **Replicas**: 2
- **Strategy**: RollingUpdate  
  - MaxUnavailable: 1  
  - MaxSurge: 1
- **Container**: todo-frontend
- **Image**: todo-chatbot-frontend:latest
- **Port**: 3000
- **LivenessProbe**: GET `/api/health` (InitialDelaySeconds: 30)
- **ReadinessProbe**: GET `/api/health` (InitialDelaySeconds: 5)
- **Resources**:  
  - Requests: 100m CPU, 128Mi Memory  
  - Limits: 500m CPU, 512Mi Memory
- **Environment Variables**:
  - `NEXT_PUBLIC_API_URL` → ConfigMap
  - `BETTER_AUTH_SECRET` → Secret

**backend-deployment**
- **Replicas**: 2
- **Strategy**: RollingUpdate
- **Container**: todo-backend
- **Image**: todo-chatbot-backend:latest
- **Port**: 8000
- **LivenessProbe**: GET `/api/health`
- **ReadinessProbe**: GET `/api/health`
- **Resources**:  
  - Requests: 200m CPU, 256Mi Memory  
  - Limits: 1000m CPU, 1Gi Memory
- **Environment Variables**:
  - `DATABASE_URL` → Secret
  - `OPENAI_API_KEY` → Secret
  - `GEMINI_API_KEY` → Secret
  - `BETTER_AUTH_SECRET` → Secret

---

### 1.2 Services

**frontend-service**
- **Type**: ClusterIP (accessible via Minikube `service` proxy)
- **Port**: 80 (TargetPort: 3000)
- **Selector**: `app: todo-frontend`

**backend-service**
- **Type**: ClusterIP
- **Port**: 8000 (TargetPort: 8000)
- **Selector**: `app: todo-backend`

---

### 1.3 Configuration

**ConfigMap: app-config**
- `NEXT_PUBLIC_API_URL` → URL for backend API (cluster-internal or proxied)
- `ENVIRONMENT`: `"development"`

**Secret: app-secrets**
- `DATABASE_URL`: Neon Connection String
- `OPENAI_API_KEY`: OpenAI Key
- `GEMINI_API_KEY`: Gemini Key
- `BETTER_AUTH_SECRET`: Authentication Secret

---

## 2. Helm Values Structure

```yaml
global:
  environment: development

frontend:
  image:
    repository: todo-chatbot-frontend
    tag: latest
    pullPolicy: Never  # Local Minikube
  replicaCount: 2
  service:
    port: 3000

backend:
  image:
    repository: todo-chatbot-backend
    tag: latest
    pullPolicy: Never
  replicaCount: 2
  service:
    port: 8000

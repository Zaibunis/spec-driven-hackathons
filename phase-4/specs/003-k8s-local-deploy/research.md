# Research: Local Kubernetes Deployment (Minikube)

**Feature**: Local Kubernetes Deployment  
**Date**: 2026-01-25  
**Branch**: 003-local-k8s-deploy  

---

## Executive Summary

This research document outlines the technical decisions and architectural considerations for deploying the Todo Chatbot application locally on Kubernetes using Minikube. The deployment includes containerization of the Next.js frontend and FastAPI backend, Helm-based packaging, secret management strategy, and AIOps tooling integration.

The goal is to provide a production-aligned yet developer-friendly local Kubernetes environment.

---

## Decision 1: Container Base Images

### Context

We need to containerize:
- Next.js frontend
- FastAPI backend

The specification mandates lightweight, secure images with minimal footprint.

### Options Considered

- **Option A: Full OS Images (Ubuntu/Debian)**  
  Large size (>500MB), broader compatibility, larger attack surface.

- **Option B: Distroless**  
  Very small and secure, but difficult to debug (no shell access).

- **Option C: Alpine / Slim Variants (Spec Mandate)**  
  `node:20-alpine` and `python:3.13-slim`.

### Decision

**Option C: Alpine / Slim**

### Rationale

- **Spec Compliance**: Explicitly required in functional requirements.
- **Image Size**: Significantly smaller, supporting <500MB target.
- **Security**: Reduced attack surface.
- **Developer Experience**: Retains shell access for debugging in local Minikube.

---

## Decision 2: Helm Chart Architecture

### Context

We need to deploy:
- Frontend (Next.js)
- Backend (FastAPI)

Both services share configuration but require independent scaling and health checks.

### Options Considered

- **Option A: Two Separate Charts**  
  Independent deployments, harder to manage shared secrets and config.

- **Option B: Umbrella Chart (Parent + Subcharts)**  
  More scalable but unnecessary complexity for two services.

- **Option C: Single Chart with Multiple Deployments**

### Decision

**Option C: Single Helm Chart**

### Rationale

- **Simplicity**: One directory (`deploy/helm/todo-chatbot`).
- **Shared Configuration**: Single `configmap.yaml` and `secrets.yaml`.
- **Atomic Deployment**: `helm install todo-chatbot` deploys all components together.
- **Monorepo Friendly**: Aligns with repository structure.

---

## Decision 3: Local Development & Secret Management

### Context

The application requires:
- OpenAI API key
- Gemini API key
- Neon PostgreSQL connection string
- JWT secrets

Secrets must be injected securely into Minikube pods.

### Options Considered

- **Option A: External Secrets Operator**  
  Production-ready but too complex for local setup.

- **Option B: SOPS (Encrypted Git Secrets)**  
  Secure but adds workflow overhead.

- **Option C: Manual Helm Secret Injection (Local values file)**

### Decision

**Option C: Manual Secret Injection via Helm**

### Rationale

- **Fast Setup**: Ideal for local-first development.
- **Low Complexity**: No extra controllers required.
- **Security**: Use `.gitignore` to exclude `values.secrets.yaml`.
- **Flexibility**: Secrets passed via `--set` or local values override file.

---

## Decision 4: Service Exposure Strategy (Minikube)

### Context

Frontend must be accessible in the browser. Backend should be accessible internally and optionally externally for debugging.

### Options Considered

- **Option A: NodePort**
- **Option B: LoadBalancer (Minikube tunnel)**
- **Option C: Ingress Controller (NGINX Ingress)**

### Decision

**Option A: NodePort (Default)**
**Option C: Ingress (Optional Advanced Setup)**

### Rationale

- **NodePort**: Simplest and works out-of-the-box with Minikube.
- **Ingress**: Can be enabled for domain-based routing if needed.
- **Avoid Complexity**: LoadBalancer requires `minikube tunnel`.

---

## Decision 5: Health Checks & High Availability

### Context

Pods must support:
- Liveness probes
- Readiness probes
- Multiple replicas (minimum 2)

### Decision

- Implement `/health` endpoint in backend.
- Use Next.js health endpoint for frontend.
- Configure:
  - `replicaCount: 2`
  - Resource limits (CPU/memory)
  - Rolling update strategy

### Rationale

- Ensures zero-downtime deployments.
- Aligns local environment with production best practices.
- Supports auto-recovery in case of pod failure.

---

## Decision 6: AIOps Integration Strategy

### Context

Enhance local Kubernetes operations using AI-powered tools.

### Tools Selected

- **kubectl-ai** (CLI assistant)
- **kagent** (Cluster agent)
- **Gordon** (Docker optimization advisor)

### Decisions

- **kubectl-ai**: Runs locally as CLI tool for debugging and cluster insights.
- **kagent**: Installed as a Deployment inside cluster to monitor logs and events.
- **Gordon**: Used during Docker build phase for optimization suggestions.

### Rationale

- Improves observability.
- Accelerates debugging.
- Encourages AI-assisted DevOps workflow.
- Maintains separation between application and tooling.

---

## Decision 7: Docker Build Strategy

### Context

We must build optimized production images for Kubernetes deployment.

### Decision

Use **multi-stage Docker builds** for both frontend and backend.

### Rationale

- Smaller final images.
- No dev dependencies in production image.
- Better layer caching.
- Improved CI/CD performance.

---

## Best Practices Applied

1. **Security First**
   - No secrets committed to Git.
   - Minimal base images.
   - Scoped environment variables.

2. **Production Parity**
   - Helm-based deployment.
   - Health checks enabled.
   - Multiple replicas configured.

3. **Stateless Architecture**
   - Backend remains stateless.
   - Database externalized.

4. **Observability**
   - Health probes.
   - Structured logging.
   - Optional AIOps tooling.

5. **Local-First Developer Experience**
   - Simple Minikube setup.
   - Helm-driven deployment.
   - Debuggable containers.

---

## Conclusion

The Local Kubernetes Deployment architecture provides:

- Lightweight and secure containerization
- Simplified Helm-based orchestration
- Secure yet practical secret management
- High availability and health monitoring
- AI-assisted operational tooling

This approach balances production alignment with local development simplicity while maintaining spec compliance and DevOps best practices.

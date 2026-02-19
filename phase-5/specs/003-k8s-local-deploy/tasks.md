---
description: "Task list for Local Kubernetes Deployment (Minikube) feature implementation"
---

# Tasks: Local Kubernetes Deployment (Minikube)

**Input**: Design documents from `/specs/004-local-k8s-deploy/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Only include optional tests if explicitly requested in the spec.

**Organization**: Tasks grouped by user story to allow independent implementation/testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)
- Include exact file paths

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize project and prepare environment for containerized deployment

- T001 Audit repository for hardcoded configuration
- T002 Extract required environment variables to `.env.example`
- T003 [P] Create `.dockerignore` for frontend in `frontend/.dockerignore`
- T004 [P] Create `.dockerignore` for backend in `backend/.dockerignore`
- T005 [P] Document environment variables in `specs/004-local-k8s-deploy/quickstart.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure setup that MUST complete before any deployment

⚠️ CRITICAL: User stories blocked until this phase is complete

- T006 Add backend health check endpoint (`backend/src/api/routes/health.py`)
- T007 Add frontend health check endpoint (`frontend/src/app/api/health/route.ts`)
- T008 [P] Initialize Helm chart structure in `deploy/helm/todo-chatbot/`
- T009 [P] Define `Chart.yaml` metadata in `deploy/helm/todo-chatbot/Chart.yaml`
- T010 [P] Create `values.yaml` with default configuration in `deploy/helm/todo-chatbot/values.yaml`

**Checkpoint**: Foundation ready for container builds and deployment

---

## Phase 3: User Story 1 - Build Production-Ready Containers (P1) 🎯 MVP

**Goal**: Build optimized Docker images for frontend and backend

**Independent Test**: Images build successfully; local Docker registry shows images; no critical vulnerabilities reported.

- T011 [P] [US1] Create multi-stage Dockerfile for frontend (`frontend/Dockerfile`)
- T012 [P] [US1] Create multi-stage Dockerfile for backend (`backend/Dockerfile`)
- T013 [P] [US1] Create `docker-compose.yml` for local testing
- T014 [US1] Build and verify frontend image locally
- T015 [US1] Build and verify backend image locally
- T016 [US1] (Optional) Analyze Dockerfiles with Gordon AI for optimization suggestions

**Checkpoint**: Images ready for Kubernetes deployment

---

## Phase 4: User Story 2 - Helm Deployment to Minikube (P1)

**Goal**: Deploy full application stack to local Minikube using Helm

**Independent Test**: `helm install` completes; all pods reach `Running`; endpoints accessible.

- T017 [P] [US2] Create ConfigMap template (`deploy/helm/todo-chatbot/templates/configmap.yaml`)
- T018 [P] [US2] Create Secret template (`deploy/helm/todo-chatbot/templates/secrets.yaml`)
- T019 [P] [US2] Create frontend Deployment template (`deploy/helm/todo-chatbot/templates/frontend-deployment.yaml`)
- T020 [P] [US2] Create backend Deployment template (`deploy/helm/todo-chatbot/templates/backend-deployment.yaml`)
- T021 [P] [US2] Create frontend Service template (`deploy/helm/todo-chatbot/templates/frontend-service.yaml`)
- T022 [P] [US2] Create backend Service template (`deploy/helm/todo-chatbot/templates/backend-service.yaml`)
- T023 [US2] Install and configure Minikube cluster (manual)
- T024 [US2] Create application namespace in Kubernetes (managed by Helm or manually)
- T025 [US2] Create local secrets file `values.secrets.yaml` (manual user-provided)
- T026 [US2] Deploy application using Helm (`helm install todo-chatbot`)
- T027 [US2] Verify pod status and check logs for startup errors

**Checkpoint**: Application stack deployed and operational

---

## Phase 4.1: User Story 3 - AIOps Integration (P2)

**Goal**: Integrate AI-assisted cluster tools (kubectl-ai, kagent, Gordon)

**Independent Test**: Tools execute commands and provide insights on cluster operations.

- T028 [US3] Install `kubectl-ai` CLI (manual)
- T029 [US3] Deploy `kagent` in Minikube cluster (manual)
- T030 [US3] Test `kubectl-ai` cluster commands (manual verification)
- T031 [US3] Test `kagent` log/event monitoring (manual verification)
- T032 [US3] Document AI-assisted cluster operation examples (`specs/004-local-k8s-deploy/quickstart.md`)

**Checkpoint**: AIOps tools operational and documented

---

## Phase 4.2: User Story 4 - Phase 3 Feature Parity (P1)

**Goal**: Ensure deployed app works identically to Phase 3 features

**Independent Test**: End-to-end user flows (Login → Chat → Create Task) succeed via Kubernetes URLs

- T033 [US4] Test frontend accessibility via Minikube service URL
- T034 [US4] Test backend API endpoint connectivity
- T035 [US4] Verify authentication flow with Better Auth
- T036 [US4] Test Neon DB connectivity
- T037 [US4] Verify chatbot functionality (text/voice)
- T038 [US4] Verify conversation state persistence across pod restarts

**Checkpoint**: Full regression testing complete

---

## Phase 4.3: Polish & Cross-Cutting Concerns

- T039 [P] Create deployment README (`deploy/README.md`)
- T040 [P] Create troubleshooting guide (`docs/troubleshooting.md`)
- T041 Record 90-second demo video of deployment and usage (manual)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Phase 1
- **US1 (Phase 3)**: Depends on Phase 2
- **US2 (Phase 4)**: Depends on US1
- **US3 (Phase 4.1)**: Depends on US2
- **US4 (Phase 4.2)**: Depends on US2

### Parallel Opportunities

- Dockerfile tasks (T011, T012) can run in parallel
- Helm template tasks (T017-T022) can run in parallel
- Documentation tasks (T039-T040) can run alongside implementation

### Implementation Strategy

1. MVP first: Setup → Foundation → Build Containers (US1) → Deploy to Minikube (US2) → Validate health
2. Add Phase 3 parity and AIOps tools (US4, US3)
3. Final polish and documentation

---

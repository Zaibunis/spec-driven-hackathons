<!-- SYNC IMPACT REPORT
Version change: N/A (initial version) → 1.0
Modified principles: None (new constitution)
Added sections: All sections are new
Removed sections: None
Templates requiring updates: ✅ All checked (plan-template.md, spec-template.md, tasks-template.md)
Follow-up TODOs: RATIFICATION_DATE needs to be set to original adoption date
-->
# Speckit.Constitution: Phase V – Advanced Cloud Deployment & Event-Driven Todo Chatbot Constitution

## Core Principles

### Event-Driven First – Loose Coupling
All inter-service communication MUST be asynchronous via Kafka events (or Dapr Pub/Sub abstraction). Direct HTTP calls between services are forbidden except via Dapr Service Invocation.

### Dapr as the Runtime Abstraction Layer
Use Dapr sidecars for ALL infrastructure interactions: Pub/Sub (Kafka/Redpanda), State Management (PostgreSQL/Neon), Jobs API (exact-time reminders – preferred over cron bindings), Secrets (Kubernetes secretstores), Service Invocation (retries, discovery, mTLS). No direct libraries (kafka-python, psycopg2, etc.) in application code.

### Scalable & Production-Grade Microservices
Break features into independent services: Chat API (producer + core logic), RecurringTaskService, NotificationService, (Optional: AuditService, WebSocketService). Services must be horizontally scalable and restart-resilient.

### Security & Portability by Design
All secrets (Neon creds, Redpanda creds, API keys) via Dapr Secrets or Kubernetes Secrets – never env vars or code. Configuration must be YAML-driven (Dapr components) for easy swap (Kafka → RabbitMQ, Neon → other DB).

### Performance, Reliability & Observability
Async Python everywhere. Target <500ms task ops, exact reminder timing (±30s). Built-in retries, circuit breakers (via Dapr). Full audit trail via task-events topic. Observability: logs, metrics, tracing enabled (Dapr defaults + kubectl).

### Development Discipline
Agentic workflow only: No freestyle coding. Every code artifact references a task ID and constitution principle. 90%+ test coverage target for new features. Local-first validation (Minikube + Redpanda Docker) before cloud.

## Technology Stack Constraints (Fixed – No Deviations)

Backend: FastAPI + SQLModel (Phase IV base), Database: Neon PostgreSQL (via Dapr State where possible), Messaging: Kafka-compatible (Redpanda preferred – serverless cloud or Strimzi self-hosted), Runtime: Dapr (full building blocks), Orchestration: Kubernetes (Minikube local → AKS/GKE/OKE cloud), CI/CD: GitHub Actions, Deployment: Helm charts (extend Phase IV), Monitoring/Logging: kubectl logs + Dapr metrics (Prometheus optional)

**Explicit Prohibitions**
- Polling loops for reminders/recurring (use Dapr Jobs API or event triggers)
- Direct Kafka client libraries in app code
- Hardcoded URLs, connection strings, or secrets
- Monolithic blocking operations
- Vendor lock-in (Dapr abstraction mandatory)

## Key Domain Rules & Constraints

Recurring Tasks: Max 10 future instances, auto-create next on completion event
Reminders: Exact-time scheduling (Dapr Jobs API), remind offset configurable, in-chat delivery (stub)
Priorities: low/medium/high enum
Tags: max 5 per task, filterable/searchable
Search/Filter/Sort: full-text, paginated, indexed queries
Events: Fixed schemas (Pydantic validated) – task-events, reminders, task-updates
Real-time Sync: Broadcast via task-updates topic + WebSocket

## Governance

Any deviation requires explicit update to this constitution (via speckit.plan proposal). All agents MUST reference constitution principles in every decision/output.

**Hierarchy of Truth**
Constitution > Specify > Plan > Tasks > Code

## Non-Functional Targets

- Task CRUD latency: <500 ms
- Reminder accuracy: within ±30 seconds
- Event throughput: 1000+ events/min (partitioned)
- Restart resilience: No data loss on pod restarts
- Multi-cloud portability: Swap Kafka/DB via YAML only

**Version**: 1.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown | **Last Amended**: 2026-02-15

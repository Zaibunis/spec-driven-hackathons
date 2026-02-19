---
id: "0001"
title: "Update Project Constitution"
stage: "constitution"
date_iso: "2026-02-15"
surface: "agent"
model: "Qwen Code"
feature: "none"
branch: "main"
user: "ZAINAB KHAN"
command: "/sp.constitution"
labels:
  - "constitution"
  - "specify"
  - "phase-v"
  - "microservices"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
prompt_text: |
  ---
  description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.
  handoffs: 
    - label: Build Specification
      agent: sp.specify
      prompt: Implement the feature specification based on the updated constitution. I want to build...
  ---

  ## User Input

  ```text
  $ARGUMENTS
  ```

  You **MUST** consider the user input before proceeding (if not empty).

  ## Outline

  You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

  Follow this execution flow:

  1. Load the existing constitution template at `.specify/memory/constitution.md`.
     - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
     **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

  2. Collect/derive values for placeholders:
     - If user input (conversation) supplies a value, use it.
     - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
     - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
     - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
       - MAJOR: Backward incompatible governance/principle removals or redefinitions.
       - MINOR: New principle/section added or materially expanded guidance.
       - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
     - If version bump type ambiguous, propose reasoning before finalizing.

  3. Draft the updated constitution content:
     - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
     - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
     - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
     - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

  4. Consistency propagation checklist (convert prior checklist into active validations):
     - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
     - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
     - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
     - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
     - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

  5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
     - Version change: old → new
     - List of modified principles (old title → new title if renamed)
     - Added sections
     - Removed sections
     - Templates requiring updates (✅ updated / ⚠ pending) with file paths
     - Follow-up TODOs if any placeholders intentionally deferred.

  6. Validation before final output:
     - No remaining unexplained bracket tokens.
     - Version line matches report.
     - Dates ISO format YYYY-MM-DD.
     - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

  7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

  8. Output a final summary to the user with:
     - New version and bump rationale.
     - Any files flagged for manual follow-up.
     - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

  Formatting & Style Requirements:

  - Use Markdown headings exactly as in the template (do not demote/promote levels).
  - Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
  - Keep a single blank line between sections.
  - Avoid trailing whitespace.

  If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

  If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

  Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

  ---

  As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

  1) Determine Stage
     - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

  2) Generate Title and Determine Routing:
     - Generate Title: 3–7 words (slug for filename)
     - Route is automatically determined by stage:
       - `constitution` → `history/prompts/constitution/`
       - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
       - `general` → `history/prompts/general/`

  3) Create and Fill PHR (Shell first; fallback agent‑native)
     - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
     - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
     - If the script fails:
       - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
       - Allocate an ID; compute the output path based on stage from step 2; write the file
       - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

  4) Validate + report
     - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
     - On failure: warn, don't block. Skip only for `/sp.phr`.


  /sp.constitution # Speckit.Constitution: Phase V – Advanced Cloud Deployment & Event-Driven Todo Chatbot

  ## Purpose & Vision
  This constitution defines the unbreakable architectural, technical, and philosophical foundation for Phase V.  
  The goal is to evolve the Phase IV Todo Chatbot into a **production-ready, scalable, event-driven microservices system** that demonstrates:
  - Decoupled services communicating solely via events
  - Portable infrastructure abstraction with Dapr
  - Advanced user features (recurring tasks, reminders, priorities, tags, search/filter/sort)
  - Local (Minikube) → Cloud (AKS/GKE/OKE) deployment readiness

  All development follows the Agentic Dev Stack:  
  Specify → Plan → Tasks → Implement (via Claude Code / AI agents).  
  No manual coding. Every line of code must trace back to a validated task.

  **Hierarchy of Truth**  
  Constitution > Specify > Plan > Tasks > Code

  ## Core Architectural Principles (Non-Negotiable)

  1. Event-Driven First – Loose Coupling  
     All inter-service communication MUST be asynchronous via Kafka events (or Dapr Pub/Sub abstraction).  
     Direct HTTP calls between services are forbidden except via Dapr Service Invocation.

  2. Dapr as the Runtime Abstraction Layer  
     Use Dapr sidecars for ALL infrastructure interactions:  
     - Pub/Sub (Kafka/Redpanda)  
     - State Management (PostgreSQL/Neon)  
     - Jobs API (exact-time reminders – preferred over cron bindings)  
     - Secrets (Kubernetes secretstores)  
     - Service Invocation (retries, discovery, mTLS)  
     No direct libraries (kafka-python, psycopg2, etc.) in application code.

  3. Scalable & Production-Grade Microservices  
     Break features into independent services:  
     - Chat API (producer + core logic)  
     - RecurringTaskService  
     - NotificationService  
     - (Optional: AuditService, WebSocketService)  
     Services must be horizontally scalable and restart-resilient.

  4. Security & Portability by Design  
     All secrets (Neon creds, Redpanda creds, API keys) via Dapr Secrets or Kubernetes Secrets – never env vars or code.  
     Configuration must be YAML-driven (Dapr components) for easy swap (Kafka → RabbitMQ, Neon → other DB).

  5. Performance, Reliability & Observability  
     Async Python everywhere. Target <500ms task ops, exact reminder timing (±30s).  
     Built-in retries, circuit breakers (via Dapr).  
     Full audit trail via task-events topic.  
     Observability: logs, metrics, tracing enabled (Dapr defaults + kubectl).

  6. Development Discipline  
     Agentic workflow only: No freestyle coding.  
     Every code artifact references a task ID and constitution principle.  
     90%+ test coverage target for new features.  
     Local-first validation (Minikube + Redpanda Docker) before cloud.

  ## Technology Stack Constraints (Fixed – No Deviations)

  - Backend: FastAPI + SQLModel (Phase IV base)  
  - Database: Neon PostgreSQL (via Dapr State where possible)  
  - Messaging: Kafka-compatible (Redpanda preferred – serverless cloud or Strimzi self-hosted)  
  - Runtime: Dapr (full building blocks)  
  - Orchestration: Kubernetes (Minikube local → AKS/GKE/OKE cloud)  
  - CI/CD: GitHub Actions  
  - Deployment: Helm charts (extend Phase IV)  
  - Monitoring/Logging: kubectl logs + Dapr metrics (Prometheus optional)

  **Explicit Prohibitions**  
  - Polling loops for reminders/recurring (use Dapr Jobs API or event triggers)  
  - Direct Kafka client libraries in app code  
  - Hardcoded URLs, connection strings, or secrets  
  - Monolithic blocking operations  
  - Vendor lock-in (Dapr abstraction mandatory)

  ## Key Domain Rules & Constraints

  - Recurring Tasks: Max 10 future instances, auto-create next on completion event  
  - Reminders: Exact-time scheduling (Dapr Jobs API), remind offset configurable, in-chat delivery (stub)  
  - Priorities: low/medium/high enum  
  - Tags: max 5 per task, filterable/searchable  
  - Search/Filter/Sort: full-text, paginated, indexed queries  
  - Events: Fixed schemas (Pydantic validated) – task-events, reminders, task-updates  
  - Real-time Sync: Broadcast via task-updates topic + WebSocket

  ## Non-Functional Targets

  - Task CRUD latency: <500 ms  
  - Reminder accuracy: within ±30 seconds  
  - Event throughput: 1000+ events/min (partitioned)  
  - Restart resilience: No data loss on pod restarts  
  - Multi-cloud portability: Swap Kafka/DB via YAML only

  ## Approval & Evolution

  Any deviation requires explicit update to this constitution (via speckit.plan proposal).  
  All agents MUST reference constitution principles in every decision/output.

  **Version:** 1.0 – High-Level Final (Phase V Complete Scope)  
  **Last Updated:** February 2026  
  **Prepared for:** Hackathon judging – clean, scalable, modern architecture showcase
response_text: |
  ## Final Summary

  I have successfully updated the project constitution at `.specify/memory/constitution.md` with the following details:

  **New Version**: 1.0 (Initial version based on provided content)
  **Version Bump Rationale**: This is the initial version of the constitution based on the Phase V requirements, replacing the template placeholders with specific architectural and development principles.

  **Files Updated**:
  - `.specify/memory/constitution.md` - Updated with the complete constitution for Phase V

  **Changes Made**:
  - Replaced all template placeholders with concrete values based on the provided Phase V content
  - Added all six core architectural principles
  - Included technology stack constraints and domain rules
  - Added governance section and non-functional targets
  - Created a Sync Impact Report at the top of the file
  - Maintained proper formatting and structure

  **Follow-up Items**:
  - The RATIFICATION_DATE is marked as a TODO since the original adoption date is unknown. This should be updated with the actual ratification date when available.

  **Suggested Commit Message**:
  `docs: add Phase V constitution for event-driven Todo Chatbot with Dapr and microservices`

  The constitution now properly reflects the requirements for Phase V - an event-driven, Dapr-enabled, microservices-based Todo Chatbot with advanced features and cloud deployment readiness.
outcome: "Successfully updated the project constitution with Phase V requirements, replacing the template placeholders with specific architectural and development principles for the event-driven Todo Chatbot with Dapr and microservices."
evaluation: "The constitution has been properly updated with all required sections, principles, and constraints for Phase V. All placeholders were replaced with concrete values based on the provided content, and the file was written correctly to .specify/memory/constitution.md."
---
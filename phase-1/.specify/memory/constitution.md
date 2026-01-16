<!-- SYNC IMPACT REPORT
Version change: 1.0.0 -> 1.1.0
Modified principles: I, II, III, IV, V, VI (updated to match new requirements)
Added sections: PROJECT OBJECTIVE, CORE PRINCIPLES, ARCHITECTURAL CONSTRAINTS, FINAL OUTCOME
Removed sections: Old phase-based principles
Templates requiring updates: ✅ updated - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Project Objective

Build a Todo Full-Stack Web Application from scratch as a modern, multi-user system with persistent storage and authentication.

The application must:
- Be implemented entirely through specs, plans, tasks, and agentic execution
- Support multiple authenticated users
- Persist data in a PostgreSQL database (Neon)
- Provide a secure REST API
- Deliver a responsive web-based user interface
- No legacy system exists. This project starts from zero.

## Core Principles

### I. Spec-first Development is Mandatory
All implementation work must be preceded by a clear, approved specification document; no code may be written without a corresponding specification; all development follows a strict spec-plan-tasks-implementation cycle.

### II. No Implementation Before Specification Approval
Development activities must not commence until specifications receive formal approval; all features must be fully specified before any implementation begins; architectural decisions must be documented before coding starts.

### III. Claude Code is the Only Entity Allowed to Write Code
All code generation must be performed exclusively by Claude Code; no manual code writing by humans is permitted; all implementation must be executed through agentic tools and automated processes.

### IV. Frontend and Backend Responsibilities Remain Strictly Separated
Frontend and backend codebases must maintain clear separation of concerns; API contracts must be defined before implementation; cross-cutting concerns must be handled through proper architectural patterns.

### V. Authentication and Authorization Enforced on Every Request
Every API endpoint must implement proper authentication and authorization checks; multi-user data isolation must be maintained at all times; security measures must be implemented consistently across all layers.

## Architectural Constraints

### Monorepo Structure
The project must use a monorepo structure following Spec-Kit Plus conventions with clear separation between frontend and backend components.

### Frontend Technology Stack
- Next.js 16+ (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui

### Backend Technology Stack
- FastAPI (Python)
- SQLModel ORM

### Database Requirements
- Neon Serverless PostgreSQL
- Proper schema design with user isolation
- Data consistency and integrity enforced

### Authentication Requirements
- Better Auth with JWT implementation
- Secure token management
- Session handling following best practices

### Package Management
- Frontend: npm
- Backend: uv

## Final Outcome

A fully functional full-stack multi-page Todo web application demonstrating:
- Proper spec-driven engineering
- Secure multi-user task isolation
- Clean monorepo organization
- End-to-end authenticated workflows

## Development Workflow

The development workflow mandates Spec-Driven Development with the following requirements:
- Every feature must have a clear specification before implementation
- All code must be generated through Claude Code (no manual coding)
- Frontend and backend remain strictly separated
- Authentication and authorization enforced on every request
- All architectural constraints must be followed
- Specifications, plans, and tasks must be maintained throughout the project lifecycle

## Governance

This constitution governs all development activities for the Todo Full-Stack Web Application project. All development must adhere to the specified principles, with AI-first tools (Claude Code, Spec-Kit Plus) exclusively used for code generation. No manual coding is permitted without prior specification approval. Compliance with architectural constraints, proper authentication/authorization, and separation of frontend and backend responsibilities is mandatory. All team members must follow the spec-driven development methodology throughout the project lifecycle.

**Version**: 1.1.0 | **Ratified**: 2025-12-22 | **Last Amended**: 2026-01-07
# Spec-Driven Hackathons

This repository contains a multi-phase project demonstrating spec-driven development using Claude Code and Spec-Kit Plus. The project evolves a simple todo application through four distinct phases, each building upon the previous one with increasing complexity and technology stack sophistication.

## 🎯 Project Overview

The project follows the **Agentic Dev Stack** workflow:
1. Write spec
2. Generate plan
3. Break into tasks
4. Implement via Claude Code

**Important**: No manual coding is allowed. All implementations must be done using Claude Code and Spec-Kit Plus, with reviews of the process, prompts, and iterations to judge each phase.

## 📚 Phases

### Phase I: Todo In-Memory Python Console App
**Objective**: Build a command-line todo application that stores tasks in memory using Claude Code and Spec-Kit Plus.

#### Basic Level Functionality
- **Goal**: Create a console-based todo application with in-memory storage
- **Approach**: Follow spec-driven development methodology with Claude Code and Spec-Kit Plus

#### Requirements
- Implement all 5 Basic Level features:
  - Add tasks
  - Delete tasks
  - Update tasks
  - View tasks
  - Mark tasks as complete
- Use spec-driven development with Claude Code and Spec-Kit Plus
- Follow clean code principles and proper Python project structure

#### Technology Stack
- UV
- Python 3.13+
- Claude Code
- Spec-Kit Plus

#### Deliverables
- GitHub repository with:
  - Constitution file
  - Specs history folder containing all specification files
  - `/src` folder with Python source code
  - README.md with setup instructions
  - CLAUDE.md with Claude Code instructions

---

### Phase II: Todo Full-Stack Web Application
**Objective**: Transform the console app into a modern multi-user web application with persistent storage using Claude Code and Spec-Kit Plus.

#### Basic Level Functionality
- **Goal**: Convert the console application into a full-stack web application with persistent storage
- **Approach**: Continue using the Agentic Dev Stack workflow with Claude Code and Spec-Kit Plus

#### Requirements
- Implement all 5 Basic Level features as a web application
- Create RESTful API endpoints
- Build responsive frontend interface
- Store data in Neon Serverless PostgreSQL database
- Authentication – Implement user signup/signin using Better Auth

#### Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 16+ (App Router) |
| Backend | Python FastAPI |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Spec-Driven | Claude Code + Spec-Kit Plus |
| Authentication | Better Auth |

#### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/{user_id}/tasks` | List all tasks |
| POST | `/api/{user_id}/tasks` | Create a new task |
| GET | `/api/{user_id}/tasks/{id}` | Get task details |
| PUT | `/api/{user_id}/tasks/{id}` | Update a task |
| DELETE | `/api/{user_id}/tasks/{id}` | Delete a task |
| PATCH | `/api/{user_id}/tasks/{id}/complete` | Toggle completion |

#### Securing the REST API: Better Auth + FastAPI Integration

**The Challenge**: Better Auth is a JavaScript/TypeScript authentication library that runs on your Next.js frontend. However, your FastAPI backend is a separate Python service that needs to verify which user is making API requests.

**The Solution**: JWT Tokens

Better Auth can be configured to issue JWT (JSON Web Token) tokens when users log in. These tokens are self-contained credentials that include user information and can be verified by any service that knows the secret key.

**How It Works**:
1. User logs in on Frontend → Better Auth creates a session and issues a JWT token
2. Frontend makes API call → Includes the JWT token in the `Authorization: Bearer <token>` header
3. Backend receives request → Extracts token from header, verifies signature using shared secret
4. Backend identifies user → Decodes token to get user ID, email, etc. and matches it with the user ID in the URL
5. Backend filters data → Returns only tasks belonging to that user

---

### Phase III: Todo AI Chatbot
**Objective**: Create an AI-powered chatbot interface for managing todos through natural language using MCP (Model Context Protocol) server architecture and Claude Code and Spec-Kit Plus.

#### Basic Level Functionality
- **Goal**: Develop a conversational interface for todo management using AI
- **Approach**: Implement using OpenAI Agents SDK and MCP server architecture

#### Requirements
- Implement conversational interface for all Basic Level features
- Use OpenAI Agents SDK for AI logic
- Build MCP server with Official MCP SDK that exposes task operations as tools
- Stateless chat endpoint that persists conversation state to database
- AI agents use MCP tools to manage tasks. The MCP tools will also be stateless and will store state in the database.

#### Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | OpenAI ChatKit |
| Backend | Python FastAPI |
| AI Framework | OpenAI Agents SDK |
| MCP Server | Official MCP SDK |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Authentication | Better Auth |

---

### Phase IV: Local Kubernetes Deployment (Minikube, Helm Charts, kubectl-ai, Kagent, Docker Desktop, and Gordon)
**Cloud Native Todo Chatbot with Basic Level Functionality**

**Objective**: Deploy the Todo Chatbot on a local Kubernetes cluster using Minikube, Helm Charts.

#### Basic Level Functionality
- **Goal**: Containerize and deploy the Todo Chatbot on a local Kubernetes cluster
- **Approach**: Use AI-assisted DevOps tools for deployment automation

#### Requirements
- Containerize frontend and backend applications (Use Gordon)
- Use Docker AI Agent (Gordon) for AI-assisted Docker operations
- Create Helm charts for deployment (Use kubectl-ai and/or kagent to generate)
- Use kubectl-ai and kagent for AI-assisted Kubernetes operations
- Deploy on Minikube locally

> **Note**: If Docker AI (Gordon) is unavailable in your region or tier, use standard Docker CLI commands or ask Claude Code to generate the docker run commands for you.

#### Technology Stack

| Component | Technology |
|-----------|------------|
| Containerization | Docker (Docker Desktop) |
| Docker AI | Docker AI Agent (Gordon) |
| Orchestration | Kubernetes (Minikube) |
| Package Manager | Helm Charts |
| AI DevOps | kubectl-ai, and Kagent |
| Application | Phase III Todo Chatbot |

## 🚀 Getting Started

Each phase has its own directory with specific setup instructions:

- [Phase I](./phase-1/README.md) - Console application setup
- [Phase II](./phase-2/README.md) - Web application setup  
- [Phase III](./phase-3/README.md) - AI chatbot setup
- [Phase IV](./phase-4/README.md) - Kubernetes deployment setup

## 🤖 Development Workflow

This project strictly follows the agentic development approach:
1. Specifications are written using Spec-Kit Plus
2. Claude Code generates implementation plans
3. Plans are broken into discrete tasks
4. Claude Code implements each task
5. No manual coding is performed

## 📁 Repository Structure

```
spec-driven-hackathons/
├── README.md                    # This file
├── phase-1/                     # Console application
│   ├── specs/                   # Specification files
│   ├── src/                     # Source code
│   ├── tests/                   # Test files
│   ├── pyproject.toml          # Project dependencies
│   └── README.md               # Phase 1 documentation
├── phase-2/                     # Web application
├── phase-3/                     # AI chatbot
└── phase-4/                     # Kubernetes deployment
```

## 🏆 Evaluation Criteria

Projects will be evaluated based on:
- Adherence to the agentic development workflow
- Quality of specifications and planning
- Implementation completeness across all phases
- Proper use of technology stacks as specified
- Code quality and architecture decisions
- Documentation and process transparency
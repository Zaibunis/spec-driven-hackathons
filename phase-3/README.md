# Todo AI Chatbot - Phase III

An AI-powered chatbot interface for managing todos through natural language using MCP (Model Context Protocol) server architecture and Claude Code with Spec-Kit Plus.

## 🎯 Objective

Create an intelligent chatbot that allows users to manage their todos through natural language conversations. The system leverages MCP server architecture to expose task operations as tools that AI agents can utilize.

## ✨ Features

- Conversational interface for todo management
- Natural language processing for task creation, modification, and deletion
- MCP server exposing task operations as tools
- Stateless chat endpoint with persistent conversation state
- AI agents utilizing MCP tools for task management
- Secure authentication system

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | OpenAI ChatKit |
| Backend | Python FastAPI |
| AI Framework | OpenAI Agents SDK |
| MCP Server | Official MCP SDK |
| ORM | SQLModel |
| Database | Neon Serverless PostgreSQL |
| Authentication | Better Auth |

## 🚀 Development Approach

This project follows the **Agentic Dev Stack workflow**:
1. Write specification
2. Generate implementation plan
3. Break into manageable tasks
4. Implement via Claude Code

> **Note**: No manual coding is allowed in this project. All implementation is done through AI-assisted development using Claude Code and Spec-Kit Plus.

## 📋 Requirements

### Basic Level Functionality
- [ ] Implement conversational interface for all basic features
- [ ] Use OpenAI Agents SDK for AI logic
- [ ] Build MCP server with Official MCP SDK that exposes task operations as tools
- [ ] Stateless chat endpoint that persists conversation state to database
- [ ] AI agents use MCP tools to manage tasks
- [ ] MCP tools are stateless and store state in the database

## 🏗️ Project Structure

```
├── backend/              # Python FastAPI backend
├── frontend/             # OpenAI ChatKit frontend
├── specs/                # Project specifications
├── .claude/              # Claude Code configuration
├── .specify/             # Spec-Kit Plus templates
├── history/              # Development history
└── README.md             # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Node.js (for frontend and MCP server)
- Python 3.9+ (for backend)
- PostgreSQL-compatible database (Neon recommended)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
# Configure your database connection in .env
python main.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### MCP Server Setup
```bash
# MCP server configuration
npm install @modelcontextprotocol/sdk
# Follow the MCP server setup guide
```

## 🧠 AI Integration

The system uses OpenAI Agents SDK to process natural language inputs and convert them into actionable todo operations. The MCP server acts as a bridge between the AI agents and the task management system.

## 🗄️ Database Schema

The application uses SQLModel ORM with Neon Serverless PostgreSQL. The schema includes:
- User authentication tables
- Conversation state storage
- Todo items with metadata
- MCP tool interaction logs

## 🔐 Authentication

The system implements Better Auth for secure user authentication and session management.

## 🤖 MCP Tools

The MCP server exposes the following tools for AI agents:
- `create_todo`: Create a new todo item
- `update_todo`: Modify an existing todo item
- `delete_todo`: Remove a todo item
- `list_todos`: Retrieve all todo items for a user
- `get_todo`: Retrieve a specific todo item

## 📊 Development Process Review

As part of the hackathon evaluation, we will review:
- The development process and methodology
- Prompts used for AI-assisted development
- Iterations and improvements made during development
- Each phase of the project implementation

## 🚧 Roadmap

- [ ] Basic todo management via chat
- [ ] Advanced natural language understanding
- [ ] Smart categorization and prioritization
- [ ] Voice input support
- [ ] Cross-platform synchronization

## 🤝 Contributing

This project is built using AI-assisted development. Contributions should follow the Agentic Dev Stack workflow:
1. Update specifications
2. Generate implementation plans
3. Use Claude Code for implementation

## 📄 License

This project is part of a hackathon submission.
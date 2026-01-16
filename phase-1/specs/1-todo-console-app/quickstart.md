# Quickstart Guide: Phase I – In-Memory Python Todo Console Application

**Feature**: 1-todo-console-app
**Date**: 2025-12-22

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. **Clone or create the project structure:**
   ```
   todo-console-app/
   ├── src/
   │   └── todo_app/
   ├── tests/
   ├── pyproject.toml
   ├── README.md
   └── CLAUDE.md
   ```

2. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run python -m src.todo_app.main
   ```

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   ├── cli/
│   │   ├── __init__.py
│   │   └── console_interface.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_task.py
│   │   └── test_task_service.py
│   └── integration/
│       └── test_console_flow.py
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_task.py

# Run tests with coverage
uv run pytest --cov=src.todo_app
```

## Key Components

### Models
- `task.py`: Defines the Task data model with validation

### Services
- `task_service.py`: Implements business logic for task operations

### CLI
- `console_interface.py`: Handles user input and menu display
- `main.py`: Application entry point

## Usage

Once the application is running, you'll see a menu with options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Follow the on-screen prompts to interact with the application.

## Development

1. **Adding new functionality**: Follow the existing pattern of separating concerns between models, services, and CLI components
2. **Testing**: Write unit tests for business logic in services and integration tests for user flows
3. **Code style**: Follow PEP 8 guidelines
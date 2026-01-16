# Todo Console Application

A Python-based console application for managing todo tasks in memory.

## Features

- Add tasks with title and description
- View all tasks with completion status
- Update task titles and descriptions
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Menu-driven console interface
- Sequential numeric task IDs
- Checkbox-style status indicators

## Prerequisites

- Python 3.13+
- UV package manager

## Installation

1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   uv run python -m src.todo_app.main
   ```

## Usage

The application provides a menu-driven interface with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

## Development

Run tests with pytest:
```bash
uv run pytest
```

## Architecture

The application follows a clean architecture with:
- Models: Data representation
- Services: Business logic
- CLI: Console interface
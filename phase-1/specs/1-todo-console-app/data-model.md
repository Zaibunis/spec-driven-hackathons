# Data Model: Phase I – In-Memory Python Todo Console Application

**Feature**: 1-todo-console-app
**Date**: 2025-12-22

## Core Entities

### Task
Represents a single todo item with the following attributes:

**Attributes:**
- `id` (int): Sequential numeric identifier, starting from 1, unique within the application session
- `title` (str): Task title, required field (cannot be empty)
- `description` (str): Task description, optional field (can be empty)
- `completed` (bool): Completion status, default is False (incomplete)

**Validation Rules:**
- ID must be a positive integer
- Title must not be empty or contain only whitespace
- Description can be empty
- Completed status is boolean (True for complete, False for incomplete)

**State Transitions:**
- `incomplete` → `complete`: When user marks task as complete
- `complete` → `incomplete`: When user marks task as incomplete

**Example:**
```python
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, eggs",
    "completed": False
}
```

## Collections

### Task List
A collection of Task entities stored in memory during the application session.

**Operations:**
- Add a new task to the list
- Retrieve all tasks
- Find a task by ID
- Update a task's title/description/completion status
- Remove a task by ID

**Constraints:**
- Task IDs must remain unique even after deletion (gaps in sequence are preserved)
- Task list exists only in memory (not persisted between application runs)
- Maximum recommended size is 1000 tasks for performance

## Relationships

### Task → Task List
- Each Task belongs to exactly one Task List during the session
- Task List can contain 0 or more Tasks
- When a Task is deleted, it's removed from the Task List
- The Task List maintains the order in which tasks were added
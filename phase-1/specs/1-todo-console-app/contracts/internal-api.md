# Internal API Contracts: Phase I – In-Memory Python Todo Console Application

**Feature**: 1-todo-console-app
**Date**: 2025-12-22

## Task Service API

### Task Creation
**Method**: `create_task(title: str, description: str = "") -> Task`
- **Input**: title (required, non-empty), description (optional)
- **Output**: Task object with assigned ID and incomplete status
- **Errors**: ValueError if title is empty

### Task Retrieval
**Method**: `get_all_tasks() -> List[Task]`
- **Input**: None
- **Output**: List of all tasks in creation order
- **Errors**: None

**Method**: `get_task_by_id(task_id: int) -> Optional[Task]`
- **Input**: task_id (positive integer)
- **Output**: Task object if found, None otherwise
- **Errors**: None

### Task Update
**Method**: `update_task(task_id: int, title: str = None, description: str = None) -> bool`
- **Input**: task_id, optional new title and/or description
- **Output**: True if successful, False if task not found
- **Errors**: ValueError if new title is empty

### Task Completion Toggle
**Method**: `mark_task_complete(task_id: int) -> bool`
- **Input**: task_id
- **Output**: True if successful, False if task not found
- **Errors**: None

**Method**: `mark_task_incomplete(task_id: int) -> bool`
- **Input**: task_id
- **Output**: True if successful, False if task not found
- **Errors**: None

### Task Deletion
**Method**: `delete_task(task_id: int) -> bool`
- **Input**: task_id
- **Output**: True if successful, False if task not found
- **Errors**: None

## Console Interface API

### Display Methods
**Method**: `display_menu() -> None`
- **Output**: Prints menu options to console

**Method**: `display_tasks(tasks: List[Task]) -> None`
- **Input**: List of Task objects
- **Output**: Prints formatted task list with checkbox indicators

### Input Methods
**Method**: `get_user_choice() -> int`
- **Output**: Integer representing user's menu selection

**Method**: `get_task_details() -> Tuple[str, str]`
- **Output**: Tuple of (title, description) from user input

**Method**: `get_task_id() -> int`
- **Output**: Integer representing task ID from user input
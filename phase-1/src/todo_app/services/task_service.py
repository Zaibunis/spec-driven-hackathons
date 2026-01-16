"""
Task service for the Todo Console Application
"""

from typing import List, Optional
from ..models.task import Task


class TaskService:
    """
    Service class to handle business logic for task operations.
    Uses in-memory storage with Python lists and dictionaries.
    """

    def __init__(self):
        """Initialize the task service with empty storage and ID counter."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with the given title and description.

        Args:
            title (str): The task title (required, non-empty)
            description (str): The task description (optional)

        Returns:
            Task: The created task with assigned ID and incomplete status

        Raises:
            ValueError: If title is empty
        """
        # Create task with next available ID
        task = Task(id=self._next_id, title=title, description=description, completed=False)

        # Add to storage
        self._tasks.append(task)

        # Increment ID for next task
        self._next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List[Task]: List of all tasks in creation order
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update a task's title and/or description by ID.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Use existing values if new values are not provided
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description

        # Validate the new title if it's being updated
        if title is not None:
            if not new_title or not new_title.strip():
                raise ValueError("Task title cannot be empty or contain only whitespace")

        # Update the task
        task.title = new_title
        task.description = new_description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Remove the task from the list (preserving ID gaps as specified in spec)
        self._tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete by ID.

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.mark_complete()
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete by ID.

        Args:
            task_id (int): The ID of the task to mark incomplete

        Returns:
            bool: True if successful, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.mark_incomplete()
        return True
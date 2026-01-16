"""
Task model for the Todo Console Application
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo item with an ID, title, description, and completion status.

    Attributes:
        id (int): Sequential numeric identifier, starting from 1, unique within the application session
        title (str): Task title, required field (cannot be empty)
        description (str): Task description, optional field (can be empty)
        completed (bool): Completion status, default is False (incomplete)
    """

    id: int
    title: str
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False

    def __str__(self):
        """String representation of the task with checkbox-style indicator."""
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.title} - {self.description}"

    def to_dict(self):
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
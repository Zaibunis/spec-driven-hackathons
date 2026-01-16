"""
Unit tests for the Task model in the Todo Console Application
"""

import pytest
from src.todo_app.models.task import Task


class TestTaskModel:
    """Test cases for the Task model."""

    def test_task_creation_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False

    def test_task_creation_defaults(self):
        """Test creating a task with default values."""
        task = Task(id=1, title="Test Task", description="Test Description")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False  # Default value

    def test_task_creation_empty_title_error(self):
        """Test that creating a task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="", description="Test Description")

    def test_task_creation_whitespace_only_title_error(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            Task(id=1, title="   ", description="Test Description")

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)

        task.mark_complete()

        assert task.completed is True

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)

        task.mark_incomplete()

        assert task.completed is False

    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task_incomplete = Task(id=1, title="Test Task", description="Test Description", completed=False)
        task_complete = Task(id=1, title="Test Task", description="Test Description", completed=True)

        expected_incomplete = "1. [ ] Test Task - Test Description"
        expected_complete = "1. [x] Test Task - Test Description"

        assert str(task_incomplete) == expected_incomplete
        assert str(task_complete) == expected_complete

    def test_task_to_dict(self):
        """Test converting a task to dictionary representation."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)

        task_dict = task.to_dict()

        expected_dict = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": True
        }

        assert task_dict == expected_dict
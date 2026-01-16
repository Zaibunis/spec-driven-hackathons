"""
Unit tests for the TaskService in the Todo Console Application
"""

import pytest
from src.todo_app.services.task_service import TaskService


class TestTaskService:
    """Test cases for the TaskService."""

    def test_initial_state(self):
        """Test that TaskService starts with empty storage and ID counter."""
        service = TaskService()

        assert len(service.get_all_tasks()) == 0
        assert service._next_id == 1

    def test_add_task(self):
        """Test adding a task."""
        service = TaskService()

        task = service.add_task("Test Title", "Test Description")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == "Test Description"
        assert task.completed is False

        tasks = service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0] == task

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        service = TaskService()

        task = service.add_task("Test Title")

        assert task.id == 1
        assert task.title == "Test Title"
        assert task.description == ""
        assert task.completed is False

    def test_add_task_empty_title_error(self):
        """Test that adding a task with empty title raises ValueError."""
        service = TaskService()

        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            service.add_task("", "Test Description")

    def test_add_task_whitespace_only_title_error(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        service = TaskService()

        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            service.add_task("   ", "Test Description")

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        service = TaskService()

        # Add some tasks
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")

        tasks = service.get_all_tasks()

        assert len(tasks) == 2
        assert tasks[0] == task1
        assert tasks[1] == task2

    def test_get_task_by_id_found(self):
        """Test getting a task by ID when it exists."""
        service = TaskService()
        task = service.add_task("Test Title", "Test Description")

        found_task = service.get_task_by_id(task.id)

        assert found_task == task

    def test_get_task_by_id_not_found(self):
        """Test getting a task by ID when it doesn't exist."""
        service = TaskService()
        service.add_task("Test Title", "Test Description")

        found_task = service.get_task_by_id(999)

        assert found_task is None

    def test_update_task_title(self):
        """Test updating a task's title."""
        service = TaskService()
        original_task = service.add_task("Original Title", "Original Description")

        success = service.update_task(original_task.id, title="New Title")

        assert success is True

        updated_task = service.get_task_by_id(original_task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "Original Description"  # Should remain unchanged

    def test_update_task_description(self):
        """Test updating a task's description."""
        service = TaskService()
        original_task = service.add_task("Original Title", "Original Description")

        success = service.update_task(original_task.id, description="New Description")

        assert success is True

        updated_task = service.get_task_by_id(original_task.id)
        assert updated_task.title == "Original Title"  # Should remain unchanged
        assert updated_task.description == "New Description"

    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        service = TaskService()
        original_task = service.add_task("Original Title", "Original Description")

        success = service.update_task(original_task.id, title="New Title", description="New Description")

        assert success is True

        updated_task = service.get_task_by_id(original_task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist."""
        service = TaskService()

        success = service.update_task(999, title="New Title")

        assert success is False

    def test_update_task_empty_title_error(self):
        """Test that updating a task with empty title raises ValueError."""
        service = TaskService()
        original_task = service.add_task("Original Title", "Original Description")

        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            service.update_task(original_task.id, title="")

    def test_update_task_whitespace_only_title_error(self):
        """Test that updating a task with whitespace-only title raises ValueError."""
        service = TaskService()
        original_task = service.add_task("Original Title", "Original Description")

        with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
            service.update_task(original_task.id, title="   ")

    def test_delete_task_success(self):
        """Test deleting an existing task."""
        service = TaskService()
        task = service.add_task("Test Title", "Test Description")

        success = service.delete_task(task.id)

        assert success is True
        assert len(service.get_all_tasks()) == 0

    def test_delete_task_not_found(self):
        """Test deleting a non-existent task."""
        service = TaskService()

        success = service.delete_task(999)

        assert success is False

    def test_delete_task_preserves_id_gaps(self):
        """Test that deleting a task preserves ID gaps (doesn't renumber remaining tasks)."""
        service = TaskService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")
        task3 = service.add_task("Task 3", "Description 3")

        # Delete the middle task
        service.delete_task(task2.id)

        # Verify that remaining tasks still have their original IDs
        remaining_tasks = service.get_all_tasks()
        assert len(remaining_tasks) == 2
        assert remaining_tasks[0].id == task1.id
        assert remaining_tasks[1].id == task3.id

    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        service = TaskService()
        task = service.add_task("Test Title", "Test Description")

        success = service.mark_task_complete(task.id)

        assert success is True

        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is True

    def test_mark_task_complete_not_found(self):
        """Test marking a non-existent task as complete."""
        service = TaskService()

        success = service.mark_task_complete(999)

        assert success is False

    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        service = TaskService()
        task = service.add_task("Test Title", "Test Description")

        # First mark as complete
        service.mark_task_complete(task.id)

        # Then mark as incomplete
        success = service.mark_task_incomplete(task.id)

        assert success is True

        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is False

    def test_mark_task_incomplete_not_found(self):
        """Test marking a non-existent task as incomplete."""
        service = TaskService()

        success = service.mark_task_incomplete(999)

        assert success is False
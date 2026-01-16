"""
Integration tests for the console flow in the Todo Console Application
"""

from unittest.mock import Mock, patch
from src.todo_app.models.task import Task
from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.console_interface import ConsoleInterface


class TestConsoleFlow:
    """Integration tests for the console application flow."""

    def setup_method(self):
        """Set up a fresh TaskService and ConsoleInterface for each test."""
        self.task_service = TaskService()
        self.console = ConsoleInterface(self.task_service)

    def test_complete_user_flow(self):
        """Test a complete user flow: add, view, update, mark complete, delete."""
        # Add a task
        task = self.task_service.add_task("Buy groceries", "Milk, bread, eggs")
        assert len(self.task_service.get_all_tasks()) == 1

        # View tasks
        tasks = self.task_service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Buy groceries"

        # Update the task
        success = self.task_service.update_task(task.id, title="Buy groceries updated", description="Milk, bread, eggs, cheese")
        assert success is True

        updated_task = self.task_service.get_task_by_id(task.id)
        assert updated_task.title == "Buy groceries updated"

        # Mark as complete
        success = self.task_service.mark_task_complete(task.id)
        assert success is True

        completed_task = self.task_service.get_task_by_id(task.id)
        assert completed_task.completed is True

        # Mark as incomplete
        success = self.task_service.mark_task_incomplete(task.id)
        assert success is True

        incomplete_task = self.task_service.get_task_by_id(task.id)
        assert incomplete_task.completed is False

        # Delete the task
        success = self.task_service.delete_task(task.id)
        assert success is True

        # Verify task is deleted
        assert len(self.task_service.get_all_tasks()) == 0

    def test_multiple_tasks_flow(self):
        """Test operations with multiple tasks."""
        # Add multiple tasks
        task1 = self.task_service.add_task("Task 1", "Description 1")
        task2 = self.task_service.add_task("Task 2", "Description 2")
        task3 = self.task_service.add_task("Task 3", "Description 3")

        # Verify all tasks exist
        tasks = self.task_service.get_all_tasks()
        assert len(tasks) == 3

        # Update middle task
        success = self.task_service.update_task(task2.id, title="Updated Task 2")
        assert success is True

        updated_task = self.task_service.get_task_by_id(task2.id)
        assert updated_task.title == "Updated Task 2"

        # Mark first task as complete
        success = self.task_service.mark_task_complete(task1.id)
        assert success is True

        completed_task = self.task_service.get_task_by_id(task1.id)
        assert completed_task.completed is True

        # Delete middle task (should preserve gaps)
        success = self.task_service.delete_task(task2.id)
        assert success is True

        # Verify remaining tasks
        remaining_tasks = self.task_service.get_all_tasks()
        assert len(remaining_tasks) == 2

        # Verify IDs are preserved (no renumbering)
        remaining_ids = [t.id for t in remaining_tasks]
        assert task1.id in remaining_ids  # First task still exists with original ID
        assert task3.id in remaining_ids  # Third task still exists with original ID
        assert task2.id not in remaining_ids  # Second task is deleted

    def test_empty_task_list_operations(self):
        """Test operations when task list is empty."""
        # Verify initial state
        tasks = self.task_service.get_all_tasks()
        assert len(tasks) == 0

        # Try to get non-existent task
        task = self.task_service.get_task_by_id(1)
        assert task is None

        # Try to update non-existent task
        success = self.task_service.update_task(1, title="New Title")
        assert success is False

        # Try to delete non-existent task
        success = self.task_service.delete_task(1)
        assert success is False

        # Try to mark non-existent task as complete
        success = self.task_service.mark_task_complete(1)
        assert success is False

        # Add a task
        task = self.task_service.add_task("Test Task", "Test Description")
        assert task.id == 1

        # Verify task exists
        tasks = self.task_service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1
"""
Integration tests for data persistence in the Todo Console Application
"""

from src.todo_app.models.task import Task
from src.todo_app.services.task_service import TaskService


class TestDataPersistence:
    """Integration tests for in-memory data persistence."""

    def setup_method(self):
        """Set up a fresh TaskService for each test."""
        self.task_service = TaskService()

    def test_data_persistence_within_session(self):
        """Test that task data persists in memory during the application session."""
        # Add tasks
        task1 = self.task_service.add_task("Task 1", "Description 1")
        task2 = self.task_service.add_task("Task 2", "Description 2")
        task3 = self.task_service.add_task("Task 3", "Description 3")

        # Verify all tasks exist
        tasks = self.task_service.get_all_tasks()
        assert len(tasks) == 3

        # Perform operations on tasks
        self.task_service.update_task(task1.id, title="Updated Task 1")
        self.task_service.mark_task_complete(task2.id)
        self.task_service.delete_task(task3.id)

        # Verify data persistence after operations
        remaining_tasks = self.task_service.get_all_tasks()
        assert len(remaining_tasks) == 2

        # Verify updates are persisted
        updated_task1 = self.task_service.get_task_by_id(task1.id)
        assert updated_task1.title == "Updated Task 1"

        # Verify completion status is persisted
        task2 = self.task_service.get_task_by_id(task2.id)
        assert task2.completed is True

        # Verify deletion is persisted
        deleted_task = self.task_service.get_task_by_id(task3.id)
        assert deleted_task is None

    def test_sequential_id_assignment_persistence(self):
        """Test that sequential ID assignment persists correctly."""
        # Add tasks
        task1 = self.task_service.add_task("Task 1", "Description 1")
        task2 = self.task_service.add_task("Task 2", "Description 2")
        task3 = self.task_service.add_task("Task 3", "Description 3")

        # Verify sequential IDs
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

        # Delete middle task
        self.task_service.delete_task(task2.id)

        # Add another task - should get next available ID
        task4 = self.task_service.add_task("Task 4", "Description 4")

        # Verify ID sequence (gaps preserved)
        assert task4.id == 4

        # Verify remaining tasks have original IDs
        remaining_tasks = self.task_service.get_all_tasks()
        remaining_ids = [task.id for task in remaining_tasks]
        assert 1 in remaining_ids  # task1
        assert 2 not in remaining_ids  # task2 deleted
        assert 3 in remaining_ids  # task3
        assert 4 in remaining_ids  # task4

    def test_id_gaps_preserved_after_deletion(self):
        """Test that ID gaps are preserved after deletion (not renumbered)."""
        # Add multiple tasks
        tasks = []
        for i in range(5):
            task = self.task_service.add_task(f"Task {i+1}", f"Description {i+1}")
            tasks.append(task)

        # Delete some tasks in the middle
        self.task_service.delete_task(tasks[1].id)  # Delete task with ID 2
        self.task_service.delete_task(tasks[3].id)  # Delete task with ID 4

        # Verify that remaining tasks still have their original IDs
        remaining_tasks = self.task_service.get_all_tasks()
        remaining_ids = [task.id for task in remaining_tasks]

        # Should have IDs 1, 3, 5 (original IDs preserved, gaps maintained)
        assert len(remaining_ids) == 3
        assert 1 in remaining_ids  # Original task 1
        assert 2 not in remaining_ids  # Deleted task 2
        assert 3 in remaining_ids  # Original task 3
        assert 4 not in remaining_ids  # Deleted task 4
        assert 5 in remaining_ids  # Original task 5

    def test_multiple_operations_persistence(self):
        """Test that multiple operations can be performed while maintaining data persistence."""
        # Add initial tasks
        task1 = self.task_service.add_task("Initial Task 1", "Initial Description 1")
        task2 = self.task_service.add_task("Initial Task 2", "Initial Description 2")

        # Update first task
        self.task_service.update_task(task1.id, title="Updated Task 1", description="Updated Description 1")

        # Mark second task as complete
        self.task_service.mark_task_complete(task2.id)

        # Add a new task
        task3 = self.task_service.add_task("New Task", "New Description")

        # Delete first task
        self.task_service.delete_task(task1.id)

        # Add another task
        task4 = self.task_service.add_task("Another Task", "Another Description")

        # Verify final state after all operations
        final_tasks = self.task_service.get_all_tasks()
        assert len(final_tasks) == 3  # task2, task3, task4 remain

        # Verify task2 is complete
        task2_updated = self.task_service.get_task_by_id(task2.id)
        assert task2_updated is not None
        assert task2_updated.completed is True
        assert task2_updated.title == "Initial Task 2"

        # Verify task3 exists with updated values
        task3_found = self.task_service.get_task_by_id(task3.id)
        assert task3_found is not None
        assert task3_found.title == "New Task"

        # Verify task4 exists
        task4_found = self.task_service.get_task_by_id(task4.id)
        assert task4_found is not None
        assert task4_found.title == "Another Task"

        # Verify task1 is deleted
        task1_found = self.task_service.get_task_by_id(task1.id)
        assert task1_found is None
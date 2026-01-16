"""
Unit tests for the ConsoleInterface in the Todo Console Application
"""

from unittest.mock import Mock, patch
from src.todo_app.models.task import Task
from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.console_interface import ConsoleInterface


class TestConsoleInterface:
    """Test cases for the ConsoleInterface."""

    def setup_method(self):
        """Set up a fresh TaskService and ConsoleInterface for each test."""
        self.task_service = TaskService()
        self.console = ConsoleInterface(self.task_service)

    def test_display_tasks_with_empty_list(self, capsys):
        """Test displaying tasks when the list is empty."""
        self.console.display_tasks([])

        captured = capsys.readouterr()
        assert "No tasks found." in captured.out

    def test_display_tasks_with_single_task(self, capsys):
        """Test displaying tasks with a single task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)
        self.console.display_tasks([task])

        captured = capsys.readouterr()
        assert "1. [ ] Test Task" in captured.out
        assert "Description: Test Description" in captured.out

    def test_display_tasks_with_completed_task(self, capsys):
        """Test displaying tasks with a completed task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=True)
        self.console.display_tasks([task])

        captured = capsys.readouterr()
        assert "1. [x] Test Task" in captured.out

    def test_display_tasks_with_multiple_tasks(self, capsys):
        """Test displaying tasks with multiple tasks."""
        task1 = Task(id=1, title="Task 1", description="Description 1", completed=False)
        task2 = Task(id=2, title="Task 2", description="Description 2", completed=True)
        self.console.display_tasks([task1, task2])

        captured = capsys.readouterr()
        assert "1. [ ] Task 1" in captured.out
        assert "2. [x] Task 2" in captured.out
        assert "Description: Description 1" in captured.out
        assert "Description: Description 2" in captured.out

    def test_display_message(self, capsys):
        """Test displaying a message."""
        self.console.display_message("Test message")

        captured = capsys.readouterr()
        assert "Test message" in captured.out

    def test_display_error(self, capsys):
        """Test displaying an error message."""
        self.console.display_error("Test error")

        captured = capsys.readouterr()
        assert "Error: Test error" in captured.out

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_valid(self, mock_input):
        """Test getting a valid user choice."""
        choice = self.console.get_user_choice()

        assert choice == 1

    @patch('builtins.input', side_effect=['invalid', '2'])
    def test_get_user_choice_invalid_then_valid(self, mock_input):
        """Test getting user choice with invalid input first."""
        choice = self.console.get_user_choice()

        assert choice == 2

    @patch('builtins.input', side_effect=['7', '1'])
    def test_get_user_choice_out_of_range_then_valid(self, mock_input):
        """Test getting user choice with out of range input first."""
        choice = self.console.get_user_choice()

        assert choice == 1

    @patch('builtins.input', side_effect=['Test Title', 'Test Description'])
    def test_get_task_details(self, mock_input):
        """Test getting task details from user input."""
        title, description = self.console.get_task_details()

        assert title == "Test Title"
        assert description == "Test Description"

    @patch('builtins.input', side_effect=['1'])
    def test_get_task_id_valid(self, mock_input):
        """Test getting a valid task ID."""
        task_id = self.console.get_task_id()

        assert task_id == 1

    @patch('builtins.input', side_effect=['0', '1'])
    def test_get_task_id_invalid_then_valid(self, mock_input):
        """Test getting task ID with invalid input first."""
        task_id = self.console.get_task_id()

        assert task_id == 1

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_get_task_id_non_numeric_then_valid(self, mock_input):
        """Test getting task ID with non-numeric input first."""
        task_id = self.console.get_task_id()

        assert task_id == 1

    @patch('builtins.input', side_effect=['New Title', 'New Description'])
    def test_get_task_update_details_both_updated(self, mock_input):
        """Test getting task update details when both fields are updated."""
        title, description = self.console.get_task_update_details()

        assert title == "New Title"
        assert description == "New Description"

    @patch('builtins.input', side_effect=['', ''])
    def test_get_task_update_details_no_updates(self, mock_input):
        """Test getting task update details when no fields are updated."""
        title, description = self.console.get_task_update_details()

        assert title is None
        assert description is None

    @patch('builtins.input', side_effect=['New Title', ''])
    def test_get_task_update_details_title_only(self, mock_input):
        """Test getting task update details when only title is updated."""
        title, description = self.console.get_task_update_details()

        assert title == "New Title"
        assert description is None

    @patch('builtins.input', side_effect=['', 'New Description'])
    def test_get_task_update_details_description_only(self, mock_input):
        """Test getting task update details when only description is updated."""
        title, description = self.console.get_task_update_details()

        assert title is None
        assert description == "New Description"

    @patch('builtins.input', side_effect=['c'])
    def test_get_completion_choice_complete(self, mock_input):
        """Test getting completion choice for 'complete'."""
        choice = self.console.get_completion_choice()

        assert choice == 'complete'

    @patch('builtins.input', side_effect=['i'])
    def test_get_completion_choice_incomplete(self, mock_input):
        """Test getting completion choice for 'incomplete'."""
        choice = self.console.get_completion_choice()

        assert choice == 'incomplete'

    @patch('builtins.input', side_effect=['invalid', 'c'])
    def test_get_completion_choice_invalid_then_valid(self, mock_input):
        """Test getting completion choice with invalid input first."""
        choice = self.console.get_completion_choice()

        assert choice == 'complete'

    def test_display_menu(self, capsys):
        """Test displaying the main menu."""
        self.console.display_menu()

        captured = capsys.readouterr()
        assert "TODO CONSOLE APPLICATION" in captured.out
        assert "1. Add Task" in captured.out
        assert "2. View Tasks" in captured.out
        assert "3. Update Task" in captured.out
        assert "4. Delete Task" in captured.out
        assert "5. Mark Task Complete/Incomplete" in captured.out
        assert "6. Exit" in captured.out
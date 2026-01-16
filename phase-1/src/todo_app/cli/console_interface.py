"""
Console interface for the Todo Console Application
"""

from typing import Optional
from ..models.task import Task
from ..services.task_service import TaskService


class ConsoleInterface:
    """
    Console interface to handle user input and display output.
    Provides menu-driven interface with numbered options.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the console interface with a task service.

        Args:
            task_service (TaskService): The task service to use for operations
        """
        self.task_service = task_service

    def display_menu(self):
        """Display the main menu options to the console."""
        print("\n" + "="*40)
        print("TODO CONSOLE APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("-"*40)

    def display_tasks(self, tasks: list):
        """
        Display a formatted list of tasks with checkbox indicators.

        Args:
            tasks (list): List of Task objects to display
        """
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            print(f"{task.id}. {status} {task.title}")
            if task.description:
                print(f"    Description: {task.description}")
        print("-" * 50)

    def get_user_choice(self) -> int:
        """
        Get the user's menu choice from console input.

        Returns:
            int: The user's menu selection (1-6)
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
            except ValueError:
                print("Please enter a valid number.")

    def get_task_details(self) -> tuple:
        """
        Get task details (title and description) from user input.

        Returns:
            tuple: (title, description) from user input
        """
        title = input("Enter task title: ").strip()
        description = input("Enter task description (optional): ").strip()
        return title, description

    def get_task_id(self) -> int:
        """
        Get a task ID from user input.

        Returns:
            int: The task ID entered by the user
        """
        while True:
            try:
                task_id = int(input("Enter task ID: "))
                if task_id > 0:
                    return task_id
                else:
                    print("Please enter a positive number for task ID.")
            except ValueError:
                print("Please enter a valid number for task ID.")

    def get_task_update_details(self) -> tuple:
        """
        Get task update details from user input.

        Returns:
            tuple: (title, description) - None if user doesn't want to update that field
        """
        print("Leave blank to keep current value.")
        title_input = input("Enter new title (or press Enter to keep current): ").strip()
        desc_input = input("Enter new description (or press Enter to keep current): ").strip()

        # Return None for fields that should not be updated
        title = title_input if title_input else None
        description = desc_input if desc_input else None

        return title, description

    def get_completion_choice(self) -> str:
        """
        Get the user's choice for marking task completion status.

        Returns:
            str: 'complete' or 'incomplete'
        """
        while True:
            choice = input("Mark as (c)omplete or (i)ncomplete? ").strip().lower()
            if choice in ['c', 'complete']:
                return 'complete'
            elif choice in ['i', 'incomplete']:
                return 'incomplete'
            else:
                print("Please enter 'c' for complete or 'i' for incomplete.")

    def display_message(self, message: str):
        """
        Display a message to the console.

        Args:
            message (str): The message to display
        """
        print(message)

    def display_error(self, error_message: str):
        """
        Display an error message to the console.

        Args:
            error_message (str): The error message to display
        """
        print(f"Error: {error_message}")
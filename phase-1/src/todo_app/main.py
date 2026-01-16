"""
Main entry point for the Todo Console Application
"""

from .services.task_service import TaskService
from .cli.console_interface import ConsoleInterface


def main():
    """Main function to run the todo console application."""
    # Initialize the task service and console interface
    task_service = TaskService()
    console = ConsoleInterface(task_service)

    print("Welcome to the Todo Console Application!")
    print("This is an in-memory todo app - tasks will be lost when you exit.")

    while True:
        # Display the menu
        console.display_menu()

        # Get user choice
        choice = console.get_user_choice()

        if choice == 1:
            # Add Task
            try:
                title, description = console.get_task_details()
                if not title:
                    console.display_error("Task title cannot be empty.")
                    continue

                task = task_service.add_task(title, description)
                console.display_message(f"Task added successfully with ID {task.id}")
            except ValueError as e:
                console.display_error(str(e))

        elif choice == 2:
            # View Tasks
            tasks = task_service.get_all_tasks()
            console.display_tasks(tasks)

        elif choice == 3:
            # Update Task
            if not task_service.get_all_tasks():
                console.display_message("No tasks available to update.")
                continue

            task_id = console.get_task_id()
            task = task_service.get_task_by_id(task_id)
            if not task:
                console.display_error("Task not found.")
                continue

            title, description = console.get_task_update_details()

            try:
                if task_service.update_task(task_id, title, description):
                    console.display_message("Task updated successfully.")
                else:
                    console.display_error("Failed to update task.")
            except ValueError as e:
                console.display_error(str(e))

        elif choice == 4:
            # Delete Task
            if not task_service.get_all_tasks():
                console.display_message("No tasks available to delete.")
                continue

            task_id = console.get_task_id()
            if task_service.delete_task(task_id):
                console.display_message("Task deleted successfully.")
            else:
                console.display_error("Task not found.")

        elif choice == 5:
            # Mark Task Complete/Incomplete
            if not task_service.get_all_tasks():
                console.display_message("No tasks available to mark.")
                continue

            task_id = console.get_task_id()
            task = task_service.get_task_by_id(task_id)
            if not task:
                console.display_error("Task not found.")
                continue

            status_choice = console.get_completion_choice()
            if status_choice == 'complete':
                if task_service.mark_task_complete(task_id):
                    console.display_message("Task marked as complete.")
                else:
                    console.display_error("Failed to mark task as complete.")
            else:  # incomplete
                if task_service.mark_task_incomplete(task_id):
                    console.display_message("Task marked as incomplete.")
                else:
                    console.display_error("Failed to mark task as incomplete.")

        elif choice == 6:
            # Exit
            console.display_message("Thank you for using the Todo Console Application!")
            break

        else:
            console.display_error("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
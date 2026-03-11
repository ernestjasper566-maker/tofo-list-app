from pathlib import Path

TASKS_FILE = Path("tasks.txt")


def load_tasks() -> list[str]:
    """Load tasks from the text file if it exists."""
    if not TASKS_FILE.exists():
        return []

    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def save_tasks(tasks: list[str]) -> None:
    """Save all tasks to the text file."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")


def add_task(tasks: list[str]) -> None:
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    save_tasks(tasks)
    print(f'Added task: "{task}"')


def view_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks: list[str]) -> None:
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to delete: ").strip()

    if not choice.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

    task_index = int(choice) - 1
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Deleted task: "{removed}"')
    else:
        print("Task number out of range.")


def show_menu() -> None:
    print("\n=== To-Do List Menu ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")


def main() -> None:
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()

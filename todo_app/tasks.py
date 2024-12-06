import json

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file."""
    if not isinstance(tasks, list):
        raise ValueError("Tasks must be a list.")
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks, start=1):  # Start numbering from 
         # Ensure task is valid before processing
        if tasks is None:
            print(f"DEBUG: Encountered None at index {i}")
            continue

        status = "✓" if t["completed"] else "✗"
        print(f"{i}. [{status}] {t['description']}")

def complete_task(index):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 1 <= index < len(tasks)+1:
        tasks[index-1]["completed"] = True
        save_tasks(tasks)

import argparse
from todo_app.tasks import add_task, list_tasks, complete_task

def main():
    parser = argparse.ArgumentParser(description="To-Do App")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add a task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Complete a task
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("index", type=int, help="Task index to complete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
        print("Task added!")
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.index)
        print("Task completed!")

if __name__ == "__main__":
    main()

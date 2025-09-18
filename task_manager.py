tasks = []

# ---------------- Core Logic Functions ----------------

def add_task_logic(name, value):
    """Add a task with name and value."""
    task = {"name": name, "value": value}
    tasks.append(task)

def remove_task_logic(index):
    """Remove task by 1-based index. Return True if successful."""
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        return True
    return False

def update_task_logic(index, new_value):
    """Update the value of a task by 1-based index. Return True if successful."""
    if 1 <= index <= len(tasks):
        tasks[index - 1]["value"] = new_value
        return True
    return False

def get_tasks():
    """Return a copy of current tasks."""
    return tasks.copy()

# ---------------- Interactive Wrappers ----------------

def add_task():
    name = input("Task name: ")
    value = input("Task info: ")
    add_task_logic(name, value)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"[{i}] {task['name']} (Info: {task['value']})")

def rmv_task():
    if not tasks:
        print("Task list is empty")
        return
    show_tasks()
    try:
        del_choice = int(input("Which task to delete? "))
    except ValueError:
        print("Invalid input")
        return

    if remove_task_logic(del_choice):
        print("Task deleted!")
    else:
        print("Invalid choice")

def set_state():
    if not tasks:
        print("No tasks to update")
        return
    show_tasks()
    try:
        choice = int(input("Which task to update? "))
    except ValueError:
        print("Invalid input")
        return
    new_value = input("New value: ")
    if update_task_logic(choice, new_value):
        print("Task updated!")
    else:
        print("Invalid choice")

# ---------------- Main Loop ----------------

def main():
    while True:
        choice = input("Do you want to add, delete, update, show, or quit?: ").strip().lower()
        if choice == "add":
            add_task()
        elif choice == "delete":
            rmv_task()
        elif choice == "update":
            set_state()
        elif choice == "show":
            show_tasks()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("SyntaxERROR: invalid input")

if __name__ == "__main__":
    main()

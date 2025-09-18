tasks = []

def add_task():
    name = input("Task: ")
    value = input("Task info: ")
    task = {"name": name, "value": value}
    tasks.append(task)



def rmv_task():
    if not tasks:
        print("task list is empty")
        return
    show_tasks()
    del_choice = int(input("Which task to delete? "))
    if 1 <= del_choice <= len(tasks):
        tasks.pop(del_choice - 1)
        print("Task deleted!")
    else:
        print("Invalid choice")

def show_tasks():
    if not tasks:
        print("No tasks")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"[{i}] {task['name']} (Info: {task['value']})")


def set_state():
    if not tasks:
        print("No tasks to update")
        return
    show_tasks()
    choice = int(input("Which task to update? "))
    if 1 <= choice <= len(tasks):
        new_value = input("New value: ")
        tasks[choice-1]["value"] = new_value
        print("Task updated!")
    else:
        print("Invalid choice")




def main():
    while True:
        choice = input("do you want to delete, add, or update a task?: ")
        if choice == "delete":
            rmv_task()
        elif choice == "add":
            add_task()
        elif choice == "update":
            set_state()
        elif choice == "quit":
            quit()
        else:
            print("SyntaxERROR: invalid Input")


if __name__ == '__main__':
    main()

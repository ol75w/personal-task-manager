tasks = []
next_id = 1

def add_task():
    global next_id

    while True:
        title = input("Task tile: ").strip()

        if title:
            break
        print("Title cannot be empty!")

    while True:
        priority = input("Enter task priority(Low, Medium, High): ").strip().capitalize()

        if priority in ["Low", "Medium", "High"]:
            break
        print("Invalid priority!Choose again!")

    task = {
        "id" : next_id,
        "title" : title,
        "priority" : priority,
        "completed": False
    }

    tasks.append(task)

    print(f"{title} added successfully!")
    print(f"Task id: {next_id}")

    next_id += 1


def view_all_task():
    if not  tasks:
        print("No task found!")
        return
    print("\n=====All Tasks=====")

    for task in tasks:
        print(f"\nId: {task['id']}")
        print(f"title: {task['title']}")
        print(f"priority: {task['priority']}")

        if task['completed']:
            print("Status: Complete")
        else:
            print("Status: Pending")
        print("----------------------")

def mark_complete():
    if not tasks:
        print("No task found!")
        return

    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("Task is already completed!")
            else:
                task["completed"] = True
                print(f"Task '{task['title']}' marked as complete!")
            return

    print("Task ID not found!")



def update_task():
    if not tasks:
        print("No task found!")
        return

    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid input! Enter a numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            print(f"Updating task: {task['title']}")
            print("1. Update Title")
            print("2. Update Priority")
            print("3. Update Both")

            choice = input("Choose an option (1-3): ").strip()

            if choice in ["1", "3"]:
                while True:
                    title = input("Enter new title: ").strip()

                    if title:
                        task["title"] = title
                        break

                    print("Title cannot be empty!")

            if choice in ["2", "3"]:
                while True:
                    priority = input(
                        "Enter new priority (Low, Medium, High): "
                    ).strip().capitalize()

                    if priority in ["Low", "Medium", "High"]:
                        task["priority"] = priority
                        break

                    print("Invalid priority!")

            if choice in ["1", "2", "3"]:
                print("Task updated successfully!")
            else:
                print("Invalid choice!")

            return

    print("Task ID not found!")






def delete_task():
    if not tasks:
        print("No task found!")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid input! Enter a numeric ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            print(f"Task found: {task['title']}")

            confirm = input(
                "Are you sure you want to delete it? (y/n): "
            ).strip().lower()

            if confirm == "y":
                tasks.remove(task)
                print("Task deleted successfully!")
            elif confirm == "n":
                print("Deletion cancelled!")
            else:
                print("Invalid choice!")

            return

    print("Task ID not found!")



def search_task():
    if not tasks:
        print("No tasks found!")
        return

    keyword = input("Enter task title to search: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty!")
        return

    found = False

    for task in tasks:
        if keyword in task["title"].lower():
            print("\n--- Task Found ---")
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Priority: {task['priority']}")

            if task["completed"]:
                print("Status: Completed")
            else:
                print("Status: Pending")

            found = True

    if not found:
        print("No matching tasks found!")


while True:

    print("====Task Menu=====")
    print("1.Add Task")
    print("2.View All Task")
    print("3.Mark As Complete")
    print("4.Update Task")
    print("5.Delete Task")
    print("6.Search Task")
    print("7.Exit")

    choice = input("Choose an option(1-7): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_all_task()

    elif choice == "3":
        mark_complete()

    elif choice == "4":
        update_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        search_task()

    elif choice == "7":
        print("Good Bye!")
        break
    else:
        print("Invalid choice!")
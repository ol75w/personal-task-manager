task = []
next_id = 1

def add_task():
    pass

def view_all_task():
    pass

def mark_complete():
    pass

def update_task():
    pass

def delete_task():
    pass

def search_task():
    pass

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
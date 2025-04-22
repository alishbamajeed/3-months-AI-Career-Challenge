
tasks = []


def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append({"task": task, "status": "Incomplete"})
    print(f"Task '{task}' has been added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet!")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['task']} - {task['status']}")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            print(f"Task '{tasks[task_num]['task']}' has been deleted!")
            tasks.pop(task_num)
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["status"] = "Completed"
            print(f"Task '{tasks[task_num]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

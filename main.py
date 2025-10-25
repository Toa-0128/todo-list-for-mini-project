# To-Do List Application

# Initialize an empty list to store tasks
tasks = []


# Function to add a task
def add_task():
    task = input("Enter the task to add: ")
    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print(f'"{task}" has been added to your tasks.')


# Function to remove a task
def remove_task():
    if not tasks:
        print("There are no tasks currently.")
        return
    print("Current tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'"{removed_task}" has been removed.')
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


# Function to view all tasks
def view_tasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("=== Task List ===")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


# Main menu loop
def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

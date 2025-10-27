# To-Do List Application

# Initialize an empty list to store tasks
tasks = []


# Function to add a task
def add_task():
    task_name = input("Enter the task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    category = input("Enter the category (e.g., Work, Study, Home): ").strip()
    if not category:
        category = "Uncategorized"

    priority = input("Enter the priority (High / Medium / Low): ").strip()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"  # Default priority

    task = {"name": task_name, "category": category, "priority": priority}
    tasks.append(task)
    print(f'Added "{task_name}" (Category: {category}, Priority: {priority})')


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
            print(f'"{removed_task["name"]}" has been removed.')
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
            print(
                f"{idx}. {task['name']} (Category: {task['category']} | Priority: {task['priority']})"
            )


# Function to view tasks by category
def view_by_category():
    if not tasks:
        print("No tasks available.")
        return

    category_name = input("Enter the category name to view: ").strip()
    found = [t for t in tasks if t["category"] == category_name]

    if not found:
        print(f'No tasks found in category "{category_name}".')
    else:
        print(f"\n=== Tasks in category: {category_name} ===")
        for idx, task in enumerate(found, start=1):
            print(f"{idx}. {task['name']} (Priority: {task['priority']})")


# Function to view tasks sorted by priority
def view_by_priority():
    if not tasks:
        print("No tasks available.")
        return

    # Define the order of priority
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order[x["priority"]])

    print("\n=== Tasks Sorted by Priority ===")
    for idx, task in enumerate(sorted_tasks, start=1):
        print(
            f"{idx}. {task['name']} (Category: {task['category']} | Priority: {task['priority']})"
        )


# Main menu loop
def main():
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. View by Category")
        print("5. View by Priority")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            view_by_category()
        elif choice == "5":
            view_by_priority()
        elif choice == "6":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

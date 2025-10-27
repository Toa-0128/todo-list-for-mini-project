# ======================================
# 🗓️ Advanced To-Do List Application
# ======================================
# Features:
# - Manage tasks by Day and Time Section (Morning / Afternoon / Evening)
# - Each task has a Category and Priority (High / Medium / Low)
# - Add, View, and Delete tasks
# ======================================

# Main data storage: nested dictionary
todo_list = {}


# -----------------------------
# Function: Add a new task
# -----------------------------
def add_task():
    day = input("Enter the day (e.g., Monday): ").capitalize()

    # Create a new day entry if it doesn't exist
    if day not in todo_list:
        todo_list[day] = {"Morning": [], "Afternoon": [], "Evening": []}

    print("\nSelect Time Section:")
    print("1. Morning")
    print("2. Afternoon")
    print("3. Evening")

    section_option = input("Choose an option: ")
    section = {"1": "Morning", "2": "Afternoon", "3": "Evening"}.get(section_option)

    if not section:
        print("Invalid option. Returning to menu.")
        return

    # Get task details
    task_name = input("Enter task name: ").strip()
    category = (
        input("Enter category (e.g., Work, Study, Home): ").strip() or "Uncategorized"
    )
    priority = input("Enter priority (High / Medium / Low): ").capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"  # Default priority

    # Create task dictionary
    task = {"name": task_name, "category": category, "priority": priority}

    # Add task to correct day and section
    todo_list[day][section].append(task)
    print(f'✅ Task "{task_name}" added to {day} - {section}')


# -----------------------------
# Function: View all tasks
# -----------------------------
def view_tasks():
    if not todo_list:
        print("No tasks saved yet.")
        return

    print("\n==== YOUR TO-DO LIST ====")
    for day, sections in todo_list.items():
        print(f"\n📅 {day}")
        for section, tasks in sections.items():
            print(f"  🌞 {section}:")
            if tasks:
                for idx, task in enumerate(tasks, 1):
                    print(
                        f"    {idx}. {task['name']} "
                        f"(Category: {task['category']} | Priority: {task['priority']})"
                    )
            else:
                print("    No tasks.")


# -----------------------------
# Function: Delete a task
# -----------------------------
def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return

    view_tasks()
    day = input("\nEnter the day to edit: ").capitalize()

    if day not in todo_list:
        print("Day not found.")
        return

    section = input("Enter section (Morning / Afternoon / Evening): ").capitalize()
    if section not in todo_list[day]:
        print("Section not found.")
        return

    if not todo_list[day][section]:
        print("No tasks in this section.")
        return

    # Show tasks in the selected section
    for idx, task in enumerate(todo_list[day][section], 1):
        print(
            f"{idx}. {task['name']} "
            f"(Category: {task['category']} | Priority: {task['priority']})"
        )

    try:
        task_index = int(input("Select the task number to delete: ")) - 1
        if 0 <= task_index < len(todo_list[day][section]):
            removed = todo_list[day][section].pop(task_index)
            print(f"🗑️ Removed: {removed['name']} from {day} - {section}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# Function: View by Priority
# -----------------------------
def view_by_priority():
    if not todo_list:
        print("No tasks saved yet.")
        return

    # Flatten all tasks into one list
    all_tasks = []
    for day, sections in todo_list.items():
        for section, tasks in sections.items():
            for t in tasks:
                all_tasks.append(
                    {
                        "day": day,
                        "section": section,
                        "name": t["name"],
                        "category": t["category"],
                        "priority": t["priority"],
                    }
                )

    # Sort by priority
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    all_tasks.sort(key=lambda x: priority_order[x["priority"]])

    print("\n==== TASKS SORTED BY PRIORITY ====")
    for idx, task in enumerate(all_tasks, 1):
        print(
            f"{idx}. {task['name']} (Day: {task['day']}, Section: {task['section']}, "
            f"Category: {task['category']}, Priority: {task['priority']})"
        )


# -----------------------------
# Menu system
# -----------------------------
def menu():
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View by Priority")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_by_priority()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")


# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    menu()

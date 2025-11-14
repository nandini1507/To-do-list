# -------------------------------
# To-Do List Application (Console)
# -------------------------------

FILENAME = "tasks.txt"


# Load tasks from a file
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


# Save tasks to a file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")


# Remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid input!")


# Update a task
def update_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nEnter task number to update: "))
        new_task = input("Enter the new task: ")
        tasks[num - 1] = new_task
        print("Task updated!")
    except (ValueError, IndexError):
        print("Invalid input!")


# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

import os

# Function to display the to-do list
def display_todo_list(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("To-Do List:")
    for task_id, task in tasks.items():
        status = "Complete" if task['complete'] else "Incomplete"
        print(f"Task ID: {task_id}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

# Function to add a task to the to-do list
def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    task_id = len(tasks) + 1
    tasks[task_id] = {'title': title, 'description': description, 'complete': False}
    print("Task added successfully.")

# Function to mark a task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter the task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]['complete'] = True
        print(f"Task ID {task_id} marked as complete.")
    else:
        print("Invalid task ID.")

# Function to delete a task from the to-do list
def delete_task(tasks):
    task_id = int(input("Enter the task ID to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task ID {task_id} deleted.")
    else:
        print("Invalid task ID.")

# Function to save tasks to a text file
def save_tasks(tasks, filename):
    with open(filename, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task['title']},{task['description']},{task['complete']}\n")

# Function to load tasks from a text file
def load_tasks(filename):
    tasks = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                task_id, title, description, complete = line.strip().split(',')
                tasks[int(task_id)] = {'title': title, 'description': description, 'complete': complete == 'True'}
    return tasks

# Main program loop
task_filename = "todo.txt"
tasks = load_tasks(task_filename)

while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_todo_list(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        mark_task_complete(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        save_tasks(tasks, task_filename)
        print("Tasks saved.")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
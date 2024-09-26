import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks available. You should add some!")
        return
    
    print("\nHere are your tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Great! Task '{title}' has been added.")

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' has been removed. Bye-bye!")
    else:
        print("Oops! That task index is not valid.")

def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Well done! Task '{tasks[task_index]['title']}' is now marked as completed.")
    else:
        print("Hmm, that task index doesn't exist.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View your tasks")
        print("2. Add a new task")
        print("3. Remove an existing task")
        print("4. Complete a task")
        print("5. Exit the application")

        choice = input("Please select an option (1-5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("What task would you like to add? ")
            add_task(tasks, title)
        elif choice == '3':
            task_index = int(input("Which task number would you like to remove? ")) - 1
            remove_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Which task number would you like to complete? ")) - 1
            complete_task(tasks, task_index)
        elif choice == '5':
            print("Thank you for using the To-Do List app. Goodbye!")
            break
        else:
            print("Hmm, that option doesn't seem to be valid. Please try again.")

if __name__ == "__main__":
    main()

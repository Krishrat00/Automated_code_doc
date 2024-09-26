```python
import json
import os

# File name for storing tasks.
TASKS_FILE = 'tasks.json'

# Loads tasks from the 'tasks.json' file.
# 
# Returns:
#     list: A list of tasks loaded from the file. If the file doesn't exist, returns an empty list.
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Saves the given list of tasks to the 'tasks.json' file.
# 
# Args:
#     tasks (list): The list of tasks to be saved.
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Displays the tasks in a formatted list.
# 
# Args:
#     tasks (list): The list of tasks to be displayed.
def display_tasks(tasks):
    if not tasks:
        print("No tasks available. You should add some!")
        return
    
    print("\nHere are your tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. [{status}] {task['title']}")

# Adds a new task to the list.
# 
# Args:
#     tasks (list): The list of tasks to which the new task will be added.
#     title (str): The title of the new task.
def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Great! Task '{title}' has been added.")

# Removes a task from the list based on its index.
# 
# Args:
#     tasks (list): The list of tasks from which the task will be removed.
#     task_index (int): The index of the task to be removed.
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' has been removed. Bye-bye!")
    else:
        print("Oops! That task index is not valid.")

# Marks a task as completed based on its index.
# 
# Args:
#     tasks (list): The list of tasks where the task will be marked as completed.
#     task_index (int): The index of the task to be marked as completed.
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Well done! Task '{tasks[task_index]['title']}' is now marked as completed.")
    else:
        print("Hmm, that task index doesn't exist.")

# The main function of the To-Do List application.
# 
# Manages the user interaction loop, handling different menu options.
def main():
    # Loads tasks from the file.
    tasks = load_tasks()
    
    # Main loop for the To-Do List application.
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

# Entry point for the program.
if __name__ == "__main__":
    main()
```

## README

# To-Do List Application

This Python script implements a simple command-line To-Do List application. Users can add, view, remove, and complete tasks. The task data is persisted in a JSON file (`tasks.json`) for future use.

## Index

* [Features](#features)
* [Usage](#usage)
* [Code Overview](#code-overview)

## Features

* **Adding Tasks:** Users can add new tasks with titles.
* **Viewing Tasks:** The application displays a list of tasks, indicating their completion status.
* **Removing Tasks:** Users can remove tasks by their index.
* **Completing Tasks:** Tasks can be marked as completed.
* **Persistence:** Task data is saved to a JSON file (`tasks.json`) for future use.

## Usage

1.  **Run the script:** Execute the Python script.
2.  **Interact with the menu:** The application presents a menu with the following options:
    * **1. View your tasks:** Displays the current tasks.
    * **2. Add a new task:** Prompts the user for a task title and adds it to the list.
    * **3. Remove an existing task:** Asks for the task index to remove.
    * **4. Complete a task:**  Asks for the task index to mark as completed.
    * **5. Exit the application:** Exits the application.
3.  **Follow the prompts:** The application provides prompts for user input.

## Code Overview

The code is structured as follows:

* **`load_tasks()`:** Loads tasks from `tasks.json`.
* **`save_tasks()`:** Saves tasks to `tasks.json`.
* **`display_tasks()`:** Displays the list of tasks.
* **`add_task()`:** Adds a new task.
* **`remove_task()`:** Removes a task by index.
* **`complete_task()`:** Marks a task as completed.
* **`main()`:** The main function that handles user interactions.

The code utilizes JSON for data storage and provides clear functions for each task management operation. 


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

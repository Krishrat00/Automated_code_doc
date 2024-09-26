```python
import json
import os

# Constant variable defining the file name for storing tasks
TASKS_FILE = 'tasks.json'

# Function to load tasks from the JSON file
def load_tasks():
    """Loads tasks from the 'tasks.json' file if it exists.

    Returns:
        list: A list of tasks loaded from the file, or an empty list if the file doesn't exist.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to the JSON file
def save_tasks(tasks):
    """Saves the provided list of tasks to the 'tasks.json' file.

    Args:
        tasks (list): The list of tasks to be saved.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks to the user
def display_tasks(tasks):
    """Displays the tasks to the user.

    Args:
        tasks (list): The list of tasks to be displayed.
    """
    if not tasks:
        print("No tasks available. You should add some!")
        return
    
    print("\nHere are your tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. [{status}] {task['title']}")

# Function to add a new task
def add_task(tasks, title):
    """Adds a new task to the list of tasks.

    Args:
        tasks (list): The list of tasks to add to.
        title (str): The title of the new task.
    """
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Great! Task '{title}' has been added.")

# Function to remove a task
def remove_task(tasks, task_index):
    """Removes a task from the list of tasks at the given index.

    Args:
        tasks (list): The list of tasks to remove from.
        task_index (int): The index of the task to remove.
    """
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' has been removed. Bye-bye!")
    else:
        print("Oops! That task index is not valid.")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    """Marks a task as completed at the given index.

    Args:
        tasks (list): The list of tasks to update.
        task_index (int): The index of the task to mark as completed.
    """
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Well done! Task '{tasks[task_index]['title']}' is now marked as completed.")
    else:
        print("Hmm, that task index doesn't exist.")

# Main function to run the To-Do List application
def main():
    """The main function of the To-Do List application.

    This function handles the user interface, user input, and calls other functions to manage tasks.
    """
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
```

```python
import json
import os

# Constant variable defining the file name for storing tasks
TASKS_FILE = 'tasks.json'

# Function to load tasks from the JSON file
def load_tasks():
    """Loads tasks from the 'tasks.json' file if it exists.

    Returns:
        list: A list of tasks loaded from the file, or an empty list if the file doesn't exist.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to the JSON file
def save_tasks(tasks):
    """Saves the provided list of tasks to the 'tasks.json' file.

    Args:
        tasks (list): The list of tasks to be saved.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks to the user
def display_tasks(tasks):
    """Displays the tasks to the user.

    Args:
        tasks (list): The list of tasks to be displayed.
    """
    if not tasks:
        print("No tasks available. You should add some!")
        return
    
    print("\nHere are your tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. [{status}] {task['title']}")

# Function to add a new task
def add_task(tasks, title):
    """Adds a new task to the list of tasks.

    Args:
        tasks (list): The list of tasks to add to.
        title (str): The title of the new task.
    """
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Great! Task '{title}' has been added.")

# Function to remove a task
def remove_task(tasks, task_index):
    """Removes a task from the list of tasks at the given index.

    Args:
        tasks (list): The list of tasks to remove from.
        task_index (int): The index of the task to remove.
    """
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' has been removed. Bye-bye!")
    else:
        print("Oops! That task index is not valid.")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    """Marks a task as completed at the given index.

    Args:
        tasks (list): The list of tasks to update.
        task_index (int): The index of the task to mark as completed.
    """
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Well done! Task '{tasks[task_index]['title']}' is now marked as completed.")
    else:
        print("Hmm, that task index doesn't exist.")

# Main function to run the To-Do List application
def main():
    """The main function of the To-Do List application.

    This function handles the user interface, user input, and calls other functions to manage tasks.
    """
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
```

## README

### Index

* [Introduction](#introduction)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)

### Introduction

This is a simple To-Do List application built using Python. It allows users to create, view, manage, and complete tasks. Tasks are stored persistently in a JSON file.

### Features

* **Add tasks:** Users can add new tasks with titles.
* **View tasks:** Users can view all tasks, including their status (completed or not).
* **Remove tasks:** Users can remove existing tasks.
* **Complete tasks:** Users can mark tasks as completed.
* **Persistent storage:** Tasks are saved in a JSON file so they are available across multiple sessions.

### Installation

To use this application, simply run the Python script `todo_list.py`.

### Usage

1. Run the script.
2. Select an option from the menu:
   * **1. View your tasks:** Displays the list of tasks.
   * **2. Add a new task:** Prompts for the task title and adds it to the list.
   * **3. Remove an existing task:** Prompts for the task index to remove and removes it.
   * **4. Complete a task:** Prompts for the task index to mark as completed and updates the status.
   * **5. Exit the application:** Exits the application.
3. Follow the prompts to interact with the application.

### Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

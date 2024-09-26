```python
import json
import os

# Constant for the tasks file name
TASKS_FILE = 'tasks.json'

# Function to load tasks from the 'tasks.json' file
def load_tasks():
    """
    Loads tasks from the 'tasks.json' file.

    Returns:
        list: A list of task dictionaries, or an empty list if the file doesn't exist.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to the 'tasks.json' file
def save_tasks(tasks):
    """
    Saves the given list of tasks to the 'tasks.json' file.

    Args:
        tasks (list): A list of task dictionaries to save.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks to the user
def display_tasks(tasks):
    """
    Displays the tasks to the user, indicating completed tasks with a checkmark (✓) and incomplete tasks with a cross (✗).

    Args:
        tasks (list): The list of tasks to display.
    """
    if not tasks:
        print("No tasks available. You should add some!")
        return
    
    print("\nHere are your tasks:")
    for index, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{index + 1}. [{status}] {task['title']}")

# Function to add a new task to the task list
def add_task(tasks, title):
    """
    Adds a new task to the task list.

    Args:
        tasks (list): The list of tasks.
        title (str): The title of the new task.
    """
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Great! Task '{title}' has been added.")

# Function to remove a task from the task list
def remove_task(tasks, task_index):
    """
    Removes a task from the task list at the specified index.

    Args:
        tasks (list): The list of tasks.
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
    """
    Marks a task as completed at the specified index.

    Args:
        tasks (list): The list of tasks.
        task_index (int): The index of the task to mark as completed.
    """
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Well done! Task '{tasks[task_index]['title']}' is now marked as completed.")
    else:
        print("Hmm, that task index doesn't exist.")

# Main function of the program
def main():
    """
    The main function that handles the user interaction and functionality of the To-Do List application.
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

## README.md

# To-Do List Application

This repository contains a simple To-Do List application written in Python. The application allows users to:

- **View their tasks**
- **Add new tasks**
- **Remove existing tasks**
- **Mark tasks as completed**

## Features

- **Persistent storage:** Tasks are saved to a JSON file (`tasks.json`) so that they are preserved between sessions.
- **User-friendly interface:** The application provides a simple menu-driven interface for easy interaction.
- **Clear task status:** Completed tasks are displayed with a checkmark (✓), while incomplete tasks are displayed with a cross (✗).

## Usage

1. **Run the `main.py` script:** You can run the application by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Interact with the menu:** The application will present you with a menu of options. Follow the prompts to perform the desired actions.

3. **Exit the application:** To exit the application, select option `5` from the menu.

## Code Structure

The code is organized into several functions:

- **`load_tasks()`**: Loads tasks from the `tasks.json` file.
- **`save_tasks()`**: Saves tasks to the `tasks.json` file.
- **`display_tasks()`**: Displays the tasks to the user.
- **`add_task()`**: Adds a new task to the task list.
- **`remove_task()`**: Removes a task from the task list.
- **`complete_task()`**: Marks a task as completed.
- **`main()`**: The main function that handles user interaction and functionality.

## Example Usage

```
To-Do List Menu:
1. View your tasks
2. Add a new task
3. Remove an existing task
4. Complete a task
5. Exit the application
Please select an option (1-5): 2
What task would you like to add? Buy groceries
Great! Task 'Buy groceries' has been added.

To-Do List Menu:
1. View your tasks
2. Add a new task
3. Remove an existing task
4. Complete a task
5. Exit the application
Please select an option (1-5): 1

Here are your tasks:
1. [✗] Buy groceries

To-Do List Menu:
1. View your tasks
2. Add a new task
3. Remove an existing task
4. Complete a task
5. Exit the application
Please select an option (1-5): 4
Which task number would you like to complete? 1
Well done! Task 'Buy groceries' is now marked as completed.

To-Do List Menu:
1. View your tasks
2. Add a new task
3. Remove an existing task
4. Complete a task
5. Exit the application
Please select an option (1-5): 1

Here are your tasks:
1. [✓] Buy groceries
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

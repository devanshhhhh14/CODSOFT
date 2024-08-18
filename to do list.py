'''A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists'''
#Features
'''Add Task: Add a new task to your to-do list.
Complete Task: Mark a task as completed by specifying its number.
Display Tasks: Show all tasks with their completion status.
Exit: Exit the application.'''

# Simple To-Do List Application

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Added task: "{task}"')

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f'Task {task_number + 1} marked as complete')
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else "✗"
                print(f'{idx + 1}. [{status}] {task["task"]}')

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add task")
            print("2. Complete task")
            print("3. Display tasks")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                task = input("Enter a new task: ")
                self.add_task(task)
            elif choice == "2":
                task_number = int(input("Enter the task number to complete: ")) - 1
                self.complete_task(task_number)
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()

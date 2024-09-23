class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task added: '{task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. [{status}] {task['task']}")

    def mark_task_complete(self, task_number):
        try:
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: '{deleted_task['task']}'")
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List App! Your Go-To App to Keep You Organized!")

    while True:
        print("\nMenu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.mark_task_complete(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
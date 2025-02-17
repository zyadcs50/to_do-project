def display_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:

        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f'Task "{task}" added to the list.')

def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" removed from the list.')
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Quit")

        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task_number = int(input("Enter task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
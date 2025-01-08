# A To-Do list

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")
    
    
def view_tasks():
    if not tasks:
        print("\nNo tasks found. Your to-do list is empty!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            
            
def add_task():
    task = input("\nEnter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty. Please try again.")

            
def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nGoodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")
            
    
if __name__ == "__main__":
    main()
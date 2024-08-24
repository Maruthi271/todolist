tasks = []

while True:
    print("\nTodo List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as done")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        task_number = int(input("Enter the task number to delete: "))
        try:
            del tasks[task_number - 1]
            print("Task deleted!")
        except IndexError:
            print("Invalid task number!")

    elif choice == "3":
        task_number = int(input("Enter the task number to mark as done: "))
        try:
            task = tasks[task_number - 1]
            tasks[task_number - 1] = f"[DONE] {task}"
            print("Task marked as done!")
        except IndexError:
            print("Invalid task number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again!")

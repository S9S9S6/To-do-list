def main():
    tasks = []  # List to store tasks

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add tasks")
        print("2. Show tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            num_of_tasks = int(input("How many tasks would you like to add? "))
            for i in range(num_of_tasks):
                task_name = input(f"Enter task {i + 1}: ")
                tasks.append({"task": task_name, "done": False})
            print("Tasks added successfully!")

        elif choice == "2":
            print("\n==== Tasks ====")
            if not tasks:
                print("No tasks available.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - [{status}]")

        elif choice == "3":
            print()
            if not tasks:
                print("No tasks to mark as done.")
            else:
                task_index = int(input("Enter the task number to mark as done: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
                  
        





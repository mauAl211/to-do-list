def main():
    to_do_list = []

    while True:
        print("To-do-list")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")
        print("5. 1-10 How'd it feel?")

        choice = input("enter your choice: ")

        if choice == '1':
            print()
            n_task = int(input(("how many tasks do you want to add: ")))
            for i in range(n_task):
                task = input("enter task: ")
                rank = int(input("Enter rank for the task (1-10): "))
                to_do_list.append({"task": task, "done": False, "rank": rank})
            print("Tasks added successfully!")

        elif choice == '2':
            print()
            print("/ntasks: ")
            for index, task in enumerate(to_do_list):
                status = "done" if task["done"] else "not done"
                rank = task.get("rank", "N/A")
                print(
                    f"{index + 1}. {task['task']} - {status} - Rank: {rank}/10")

        elif choice == '3':
            print()
            print("\nTasks: ")
            task_index = int(
                input("Enter the task number to mark as done:")) - 1
            if 0 <= task_index < len(to_do_list):
                to_do_list[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")

        elif choice == '4':
            print("Exiting the program.")
            break

        elif choice == '5':
            print(
                "1 - 10 How'd it feel?")
            try:
                rank = int(input("Enter your rank (1-10): "))
                if 1 <= rank <= 10:
                    print(
                        f"Thank you for your feedback! You rated it: {rank}/10")
                else:
                    print("Invalid rank. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()

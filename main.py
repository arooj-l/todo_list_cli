
# initialize list to store tasks
tasks = []

while True:
    print("""
        \n***** Todo list Menu *****
                1: ADD task
                2: VIEW task
                3: REMOVE task
                4: EXIT
                5:CLEAR all tasks
      """)
     
    
    choice = input("choose an option(1-4): ")

    if choice == "1":
        task  = input("Enter a task: ")
        tasks.append(task)
        print("task added")

    elif choice == "2":
        print("\nYour tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks, start =1):
                print(f"{index}.{task}")
    
    elif choice == "3":
        if not tasks:
           print("The task is list is empty")
        else:
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                

    elif choice == "4":
         print("Goodbye!")
         break
    elif choice == "5":
         tasks.clear()
         print("List is clear now")
    
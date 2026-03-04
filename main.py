
# initialize list to store tasks
tasks = []
try:
    while True:

     print("""
        \n***** Todo list Menu *****
                1: ADD task
                2: VIEW task
                3: REMOVE task
                4: EXIT
      """)
     
    
     choice = input("choose an option(1-4): ")

     if choice == "1":
        task  = input("Enter a task: ")
        tasks.append(task)
        print("task added")

     elif choice == "2":
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start =1):
            print(f"{index}.{task}")
    
     elif choice == "3":
        if not tasks:
           print("The task is list is empty")
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        print(f"Removed: {removed}")

     elif choice == "4":
         print("Goodbye!")
         break
     elif choice == "5":
         tasks.clear()
         print("List is clear now")
    


     else:
        print("Invalid choice. Try again.")
except ValueError:
    print("Enter a valid number")

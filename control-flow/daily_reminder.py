task = input("Enter your task:")
Priority = input("Priority (high, medium, low):").lower()
time_bound = input("Is it time-bound? (yes or no):").lower()

match Priority: 
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is high priority task.")
    case "medium":
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "no":
            print(f"Reminder: '{task}' it is a low priority task. Consider compleating it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority time-bounded task.")
    case _:
        print("Invalid priority or time-bounded entered. Please enter the correct input.")

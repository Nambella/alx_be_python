task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Ensure case-insensitive input
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority time-bound task.")
    case _:
        print("Invalid priority or time-bound entered. Please enter the correct input.")
task = input("Enter your task: "). lower ()
Priority = input("Enter the task's priority (high, medium, low): "). lower ()
time_bound = input("Is it time-bound? (yes or no): "). lower ()
if Priority == "high":
    if time_bound == "yes":
        print(f"Reminder: {task} (High priority) that requires immediate attention today!")
    else:
        print(f"Reminder: {task} (High priority)")
elif Priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: {task} (Medium priority) that requires immediate attention today!")
    else:
        print(f"Reminder: {task} (Medium priority)")
elif Priority == "low":
    if time_bound == "yes":
        print(f"Reminder: {task} (Low priority) that requires immediate attention today!")
    else:
        print(f"Reminder: {task} (Low priority)")
else:
    print("Invalid priority level. Please choose high, medium, or low.")

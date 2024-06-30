task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")
if priority == "high" :
    if time_bound.lower() == "yes" :
        print(f"Reminder: {task} (High priority) that requires immediate attention today!")
    else:
        print(f"Reminder: {task} (High priority)")
elif priority == "medium" :
    if time_bound.lower() == "yes" :
        print(f"Reminder: {task} (Medium priority) that requires immediate attention today!")
    else:
        print(f"Reminder: {task} (Medium priority)")
elif priority == "low" :
    if time_bound.lower() == "yes" :
        print(f"Reminder: {task} (Low priority) that requires immediate attention today!")
    else :
        print(f"Reminder: {task} (Low priority)")
else :
    print("Invalid priority level. Please choose high, medium, or low.")

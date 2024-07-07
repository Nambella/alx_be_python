import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

display_current_datetime()
def calculate_future_date():
    try:
        num_days = int(input("Enter the number of days to add: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=num_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date after {num_days} days: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

calculate_future_date()


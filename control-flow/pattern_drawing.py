# Prompt user for input
try:
    size = int(input("Enter the size of the pattern (positive integer): "))
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # Draw the pattern
        for _ in range(size):
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next row
except ValueError:
    print("Invalid input. Please enter a positive integer.")


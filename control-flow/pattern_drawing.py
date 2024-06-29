try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
    else:
        # Draw the pattern
        for _ in range(size):
            for _ in range(size):
                print("*", end="")
            print()  
except ValueError:
    print("Invalid input. Please enter a positive integer.")
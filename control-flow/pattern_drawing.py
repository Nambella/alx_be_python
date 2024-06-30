def main():
    try:
        # Prompt user for pattern size
        size = int(input("Enter the size of the pattern: "))
        # Draw the square pattern
        for row in range(size):
            for col in range(size):
                print("*", end="")
            print()  # Move to the next row
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
if __name__ == "__main__":
    main()

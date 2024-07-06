# pattern_drawing.py
def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Draw the pattern
        for _ in range(size):
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next row

    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()

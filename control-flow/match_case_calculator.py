# match_case_calculator.py

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform calculation using Match Case
        result = match_case_calculate(num1, num2, operation)

        # Display the result
        print(f"The result is {result:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

def match_case_calculate(num1, num2, operation):
    # Perform calculation based on user's choice
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
        case _:
            return "Invalid operation"

if __name__ == "__main__":
    main()

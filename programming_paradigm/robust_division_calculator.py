import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)
def robust_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(robust_division(num1, num2))
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(robust_division(num1, num2))
if __name__ == "__main__":
    main()
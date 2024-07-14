def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
    except ZeroDivisionError:
        return "Error: cannot divide by zero."
    except ValueError:
        return "Error: Non-numeric input provided. Please enter valid numbers."
    return result
def robust_division_calculator(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    return result

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(robust_division_calculator(num1, num2))

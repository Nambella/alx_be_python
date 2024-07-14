def robust_division_calculator(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except EOFError:
        return "Error: No input provided."
    return result

# Example usage with default values for testing
num1 = 12  # Default value for testing
num2 = 2   # Default value for testing
print(f"The result of the division is {robust_division_calculator(num1, num2)}")

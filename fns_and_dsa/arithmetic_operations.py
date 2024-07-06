# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        num1 (float): First numerical value.
        num2 (float): Second numerical value.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', or 'divide').

    Returns:
        float: Result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: divided by zero"

if __name__ == "__main__":
    result = perform_operation(10, 5, 'add')
    print(f"Result of addition: {result}")


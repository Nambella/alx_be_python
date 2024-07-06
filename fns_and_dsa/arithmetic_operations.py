def perform_operation(operation, num1, num2):
    """
    Performs basic arithmetic operations on two numbers.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the arithmetic operation.
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
            raise ValueError("Cannot divide by zero.")


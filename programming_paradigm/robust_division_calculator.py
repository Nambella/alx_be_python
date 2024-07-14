def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Non-numeric input provided. Please enter valid numbers."
    return result

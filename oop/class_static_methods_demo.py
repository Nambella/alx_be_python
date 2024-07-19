class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage:
if __name__ == "__main__":
    result_add = Calculator.add(3, 5)
    print(f"Sum: {result_add}")

    result_multiply = Calculator.multiply(4, 6)
    print(f"Product: {result_multiply}")

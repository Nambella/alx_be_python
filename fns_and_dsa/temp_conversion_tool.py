FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        user_input = input("Enter a temperature (e.g., 98.6 F or 37.0 C): ")
        temp, unit = user_input.split()
        temp = float(temp)

        if unit.lower() == 'f':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp:.2f} degrees F is {converted_temp:.2f} degrees C.")
        elif unit.lower() == 'c':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp:.2f} degrees C is {converted_temp:.2f} degrees F.")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'F' or 'C'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


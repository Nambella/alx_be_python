CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        user_input = input("Enter a temperature (e.g., 100F or 37C): ")
        if user_input[-1].lower() == 'f':
            temperature = float(user_input[:-1])
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is equivalent to {converted_temp:.2f} Fahrenheit.")
        else:
            raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'F' or 'C'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

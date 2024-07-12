# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User input
        temperature = float(input("Enter a temperature: "))
        unit = input("Is it in Celsius (C) or Fahrenheit (F)? ").upper()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is equivalent to {converted_temp:.2f}°F.")
        elif unit == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is equivalent to {converted_temp:.2f}°C.")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

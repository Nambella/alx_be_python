CELSIUSTOFAHRENHEITFACTOR = (9/5)
FAHRENHEITTOCELSIUSFACTOR = (5/9)
def converttocelsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEITTOCELSIUSFACTOR
    return celsius
def converttofahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUSTOFAHRENHEITFACTOR) + 32
    return fahrenheit
def main():
    try:
        user_input = input("Enter a temperature: ")
        if user_input[-1].lower() == 'f':
            temperature = float(user_input[:-1])
            converted_temp = converttocelsius(temperature)
            print(f"{temperature} Fahrenheit is equivalent to {converted_temp:.2f} Celsius.")
        elif user_input[-1].lower() == 'c':
            temperature = float(user_input[:-1])
            converted_temp = converttofahrenheit(temperature)
            print(f"{temperature} Celsius is equivalent to {converted_temp:.2f} Fahrenheit.")
        else:
            raise ValueError("Invalid temperature format. Please enter a numeric value followed by 'F' or 'C'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()
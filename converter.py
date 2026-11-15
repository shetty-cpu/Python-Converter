
# Python Converter Project

# Conversion factors
CONVERSIONS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}

def arithmetic():
    print("\n--- Basic Arithmetic ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose operation: ")

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")

def km_to_miles():
    try:
        km = float(input("Enter distance in kilometres: "))

        if km < 0:
            print("Distance cannot be negative.")
            return

        miles = km * CONVERSIONS["km_to_miles"]
        print("Distance in miles:", round(miles, 2))

    except ValueError:
        print("Please enter a valid number.")

def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter temperature in Celsius: "))

        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit:", round(fahrenheit, 2))

    except ValueError:
        print("Please enter a valid number.")

def kg_to_pounds():
    try:
        kg = float(input("Enter weight in kilograms: "))

        if kg < 0:
            print("Weight cannot be negative.")
            return

        pounds = kg * CONVERSIONS["kg_to_pounds"]
        print("Weight in pounds:", round(pounds, 2))

    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== PYTHON CONVERTER =====")
        print("1. Basic Arithmetic")
        print("2. Kilometres to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. Kilograms to Pounds")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            arithmetic()
        elif choice == "2":
            km_to_miles()
        elif choice == "3":
            celsius_to_fahrenheit()
        elif choice == "4":
            kg_to_pounds()
        elif choice == "5":
            print("Thank you for using Python Converter!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
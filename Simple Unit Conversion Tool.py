# Simple Unit Conversion Tool
def unit_converter():
    print("Unit Converter Menu:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kg is equal to {pounds:.2f} lbs")
    elif choice == 2:
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} lbs is equal to {kilograms:.2f} kg")
    elif choice == 3:
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} m is equal to {feet:.2f} ft")
    elif choice == 4:
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} ft is equal to {meters:.2f} m")
    elif choice == 5:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == 6:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice! Please select between 1 and 6.")


# Call the function
unit_converter()

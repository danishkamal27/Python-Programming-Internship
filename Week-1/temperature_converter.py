"""
Temperature Converter
Python Programming Internship - Week 1: Assignment 1

Converts temperature values between Celsius and Fahrenheit using modular functions.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit using the formula (C * 9/5) + 32."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius using the formula (F - 32) * 5/9."""
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=" * 35)
    print("      Temperature Converter")
    print("=" * 35)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    print("=" * 35)

    while True:
        choice = input("\nEnter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"\nResult: {celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
            except ValueError:
                print("Invalid input! Please enter a valid numerical temperature.")
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"\nResult: {fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius")
            except ValueError:
                print("Invalid input! Please enter a valid numerical temperature.")
        elif choice == '3':
            print("Thank you for using Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

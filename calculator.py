"""
Assignment 3: Calculator Class with Exception Handling
Demonstrates Object-Oriented Programming (OOP) with robust exception handling
and defensive programming in Python.
"""


class Calculator:
    """Class implementing basic arithmetic operations with exception handling."""

    def add(self, a, b):
        """Perform addition of two numbers."""
        try:
            num_a, num_b = float(a), float(b)
            return num_a + num_b
        except (ValueError, TypeError) as e:
            print(f"[ERROR] Input Error [Addition]: Invalid numeric operands '{a}', '{b}'. ({e})")
            return None

    def subtract(self, a, b):
        """Perform subtraction of two numbers."""
        try:
            num_a, num_b = float(a), float(b)
            return num_a - num_b
        except (ValueError, TypeError) as e:
            print(f"[ERROR] Input Error [Subtraction]: Invalid numeric operands '{a}', '{b}'. ({e})")
            return None

    def multiply(self, a, b):
        """Perform multiplication of two numbers."""
        try:
            num_a, num_b = float(a), float(b)
            return num_a * num_b
        except (ValueError, TypeError) as e:
            print(f"[ERROR] Input Error [Multiplication]: Invalid numeric operands '{a}', '{b}'. ({e})")
            return None

    def divide(self, a, b):
        """Perform division of two numbers with ZeroDivisionError handling."""
        try:
            num_a, num_b = float(a), float(b)
            if num_b == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return num_a / num_b
        except ZeroDivisionError as e:
            print(f"[ERROR] Math Error [Division]: Cannot divide {a} by zero! ({e})")
            return None
        except (ValueError, TypeError) as e:
            print(f"[ERROR] Input Error [Division]: Invalid numeric operands '{a}', '{b}'. ({e})")
            return None


def demonstrate_calculator():
    """Demonstrate Calculator class operations and exception handling capabilities."""
    print("=========================================")
    print("   DEMONSTRATING CALCULATOR CLASS        ")
    print("=========================================\n")

    calc = Calculator()

    print("--- 1. Standard Arithmetic Operations ---")
    res_add = calc.add(15, 25)
    print(f" 15 + 25 = {res_add}")

    res_sub = calc.subtract(50, 18.5)
    print(f" 50 - 18.5 = {res_sub}")

    res_mul = calc.multiply(6, 7)
    print(f" 6 * 7 = {res_mul}")

    res_div = calc.divide(100, 4)
    print(f" 100 / 4 = {res_div}")

    print("\n--- 2. Exception Handling: Division by Zero ---")
    res_zero = calc.divide(50, 0)
    print(f" Result of 50 / 0: {res_zero}")

    print("\n--- 3. Exception Handling: Invalid Input (Non-numeric strings) ---")
    res_invalid_1 = calc.add("ten", 20)
    res_invalid_2 = calc.divide(100, "abc")
    res_invalid_3 = calc.multiply(None, 5)

    print("\n--- 4. String Numbers Conversion Test ---")
    res_str = calc.add("45.5", "54.5")
    print(f" '45.5' + '54.5' = {res_str}")


if __name__ == "__main__":
    demonstrate_calculator()

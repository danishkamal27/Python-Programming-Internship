"""
Even/Odd & Prime Number Checker
Python Programming Internship - Week 1: Assignment 3

Checks if an integer is even or odd, and determines whether it is a prime number.
"""

def is_even(number: int) -> bool:
    """Return True if the number is even, False if odd."""
    return number % 2 == 0


def is_prime(number: int) -> bool:
    """
    Determine if a number is prime.
    
    Rules:
    - Numbers <= 1 (including 0 and negative numbers) are NOT prime.
    - 2 is the only even prime number.
    - Numbers divisible by any integer from 2 up to sqrt(number) are NOT prime.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Check odd divisors up to square root of number
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
        
    return True


def main():
    print("=" * 40)
    print("  Even/Odd & Prime Number Checker")
    print("=" * 40)

    while True:
        try:
            user_input = input("\nEnter an integer (or type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Thank you for using the checker. Goodbye!")
                break
                
            num = int(user_input)
            
            # Determine even/odd status
            parity = "Even" if is_even(num) else "Odd"
            
            # Determine prime status
            prime_status = "a Prime number" if is_prime(num) else "NOT a Prime number"
            
            print(f"\nResults for {num}:")
            print(f"  • Parity : {parity}")
            print(f"  • Status : {num} is {prime_status}.")
            print("-" * 40)

        except ValueError:
            print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()

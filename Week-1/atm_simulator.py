"""
Simple ATM Simulator
Python Programming Internship - Week 1: Mini Project

An interactive educational command-line ATM simulation supporting PIN login,
balance check, deposit, and withdrawal operations using modular functions.
"""

# Sample / Demo PIN for testing
DEMO_PIN = "1234"
MAX_ATTEMPTS = 3


def check_balance(balance: float) -> None:
    """Display current account balance formatted as currency."""
    print(f"\nYour current balance is: ${balance:.2f}")


def deposit(balance: float, amount: float) -> float:
    """
    Deposit funds into account.
    Rejects zero or negative amounts. Returns updated balance.
    """
    if amount <= 0:
        print("\n[Error] Invalid deposit amount! Amount must be greater than $0.00.")
        return balance
    
    new_balance = balance + amount
    print(f"\n[Success] Deposited ${amount:.2f} successfully.")
    print(f"Updated balance: ${new_balance:.2f}")
    return new_balance


def withdraw(balance: float, amount: float) -> float:
    """
    Withdraw funds from account.
    Rejects zero/negative amounts and prevents overdrawing.
    Returns updated balance.
    """
    if amount <= 0:
        print("\n[Error] Invalid withdrawal amount! Amount must be greater than $0.00.")
        return balance
    
    if amount > balance:
        print(f"\n[Error] Insufficient funds! Available balance is ${balance:.2f}.")
        return balance
    
    new_balance = balance - amount
    print(f"\n[Success] Withdrew ${amount:.2f} successfully.")
    print(f"Updated balance: ${new_balance:.2f}")
    return new_balance


def authenticate_user() -> bool:
    """
    Prompt user for PIN and authenticate against DEMO_PIN.
    Allows up to MAX_ATTEMPTS tries.
    """
    print("=" * 40)
    print("      Welcome to Simple ATM System")
    print("=" * 40)
    
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        entered_pin = input("Enter your 4-digit PIN: ").strip()
        if entered_pin == DEMO_PIN:
            print("\n[Access Granted] Login successful!")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"[Access Denied] Incorrect PIN. Remaining attempts: {remaining}\n")
            else:
                print("\n[Account Locked] Too many incorrect PIN attempts.")
                return False
    return False


def display_menu() -> None:
    """Display ATM main menu choices."""
    print("\n" + "=" * 40)
    print("              ATM MENU")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("=" * 40)


def main():
    if not authenticate_user():
        print("Exiting application...")
        return

    # Initial starting balance
    balance = 1000.00

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            try:
                amt = float(input("Enter deposit amount: $"))
                balance = deposit(balance, amt)
            except ValueError:
                print("\n[Error] Invalid amount! Please enter a valid number.")
        elif choice == '3':
            try:
                amt = float(input("Enter withdrawal amount: $"))
                balance = withdraw(balance, amt)
            except ValueError:
                print("\n[Error] Invalid amount! Please enter a valid number.")
        elif choice == '4':
            print("\nThank you for using Simple ATM System. Have a great day!")
            break
        else:
            print("\n[Error] Invalid option! Please select a choice between 1 and 4.")


if __name__ == "__main__":
    main()

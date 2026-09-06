"""
Assignment 1: Bank Account Class
Demonstrates Object-Oriented Programming (OOP) concepts such as classes,
objects, encapsulation, and input validation.
"""


class BankAccount:
    """Class representing a bank account with basic banking operations."""

    def __init__(self, account_number, account_holder, initial_balance=0.0):
        """Initialize bank account with account number, holder name, and starting balance."""
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(initial_balance) if initial_balance >= 0 else 0.0

    def deposit(self, amount):
        """Deposit a specified positive amount into the account."""
        if amount <= 0:
            print(f"[FAILED] Deposit failed: Amount must be greater than $0.00. (Attempted: ${amount:.2f})")
            return False

        self.balance += amount
        print(f"[SUCCESS] Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw a specified positive amount from the account if funds are sufficient."""
        if amount <= 0:
            print(f"[FAILED] Withdrawal failed: Amount must be greater than $0.00. (Attempted: ${amount:.2f})")
            return False

        if amount > self.balance:
            print(f"[FAILED] Withdrawal failed: Insufficient funds. Available: ${self.balance:.2f}, Requested: ${amount:.2f}")
            return False

        self.balance -= amount
        print(f"[SUCCESS] Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        return True

    def display_balance(self):
        """Display the current balance and account summary."""
        print("-" * 45)
        print(f" Account Number : {self.account_number}")
        print(f" Account Holder : {self.account_holder}")
        print(f" Current Balance: ${self.balance:.2f}")
        print("-" * 45)


def demonstrate_bank_account():
    """Demonstrate BankAccount functionality and edge case validations."""
    print("=========================================")
    print("   DEMONSTRATING BANK ACCOUNT CLASS      ")
    print("=========================================\n")

    # Creating Bank Account objects
    acc1 = BankAccount(account_number="ACC-1001", account_holder="Alice Johnson", initial_balance=500.00)
    acc2 = BankAccount(account_number="ACC-1002", account_holder="Bob Smith", initial_balance=200.00)

    print("--- Initial Account States ---")
    acc1.display_balance()
    acc2.display_balance()

    print("\n--- Valid Deposit & Withdrawal ---")
    acc1.deposit(150.50)
    acc1.withdraw(200.00)
    acc1.display_balance()

    print("\n--- Edge Case 1: Negative / Zero Deposit ---")
    acc1.deposit(-50.00)
    acc1.deposit(0.00)

    print("\n--- Edge Case 2: Insufficient Funds Withdrawal ---")
    acc2.withdraw(500.00)

    print("\n--- Edge Case 3: Invalid Withdrawal Amount ---")
    acc2.withdraw(-25.00)

    print("\n--- Final Account States ---")
    acc1.display_balance()
    acc2.display_balance()


if __name__ == "__main__":
    demonstrate_bank_account()

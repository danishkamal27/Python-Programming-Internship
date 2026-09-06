# Week 3 — Object-Oriented Programming (OOP) & Exception Handling

Welcome to **Week 3** of the Python Programming Internship repository! This week focuses on core **Object-Oriented Programming (OOP)** concepts, class interactions, encapsulation, defensive programming with validation, and robust **Exception Handling** in Python.

---

## 📚 Topics & Concepts Covered
- **Classes & Objects**: Defining classes, instantiating objects, instance attributes, and methods using `self`.
- **Encapsulation & Validation**: Protecting internal state and validating method inputs to prevent invalid state mutations.
- **Class Interaction**: Passing objects to other objects and managing collections of custom objects.
- **Exception Handling**: Using `try-except-raise` blocks to handle arithmetic errors (`ZeroDivisionError`) and invalid type conversions (`ValueError`, `TypeError`).
- **Data Formatting**: Generating clean ASCII tables for business invoices.

---

## 📁 Week 3 Directory Structure

```text
Week-3/
├── README.md            # Documentation for Week 3
├── bank_account.py      # Assignment 1: Bank Account Class with Validation
├── library_system.py   # Assignment 2: Library Management System (OOP)
├── calculator.py        # Assignment 3: Calculator Class with Exception Handling
└── billing_system.py    # Mini Project: OOP-Based Billing System
```

---

## 📋 Assignment Summaries & Features

### 1. Bank Account Class (`bank_account.py`)
- **Description**: Demonstrates basic OOP concepts by modeling a bank account.
- **Key Features**:
  - `BankAccount` class with `account_number`, `account_holder`, and `balance` attributes.
  - Core banking operations: `deposit()`, `withdraw()`, and `display_balance()`.
  - Comprehensive validation: prevents negative deposits/withdrawals and handles insufficient balance attempts gracefully.

### 2. Library Management System (`library_system.py`)
- **Description**: An OOP library catalog system managing book transactions.
- **Key Features**:
  - `Book` class (`book_id`, `title`, `author`, `is_issued`).
  - `Library` class manages a catalog of `Book` objects.
  - Supported operations: `add_book()`, `remove_book()`, `issue_book()`, `return_book()`, `display_books()`.
  - Edge case handling: trying to issue an already issued or non-existent book, returning a book that was never issued, and preventing removal of currently issued books.

### 3. Calculator Class with Exception Handling (`calculator.py`)
- **Description**: A class-based calculator featuring robust exception handling.
- **Key Features**:
  - Implements `add()`, `subtract()`, `multiply()`, and `divide()`.
  - Explicit handling for `ZeroDivisionError` when dividing by zero.
  - Exception handling for `ValueError` and `TypeError` when invalid non-numeric arguments are supplied.

### 4. Mini Project: Billing System (`billing_system.py`)
- **Description**: An OOP-based store billing system that generates formatted invoices.
- **Key Features**:
  - `Product` class (`name`, `price`, `quantity`, `get_total()`).
  - `Bill` class manages list of `Product` items and configurable tax rate.
  - Automatic calculation of subtotal, tax amount, and grand total.
  - Renders the final bill in a clean, professional **TABULAR FORMAT**.

---

## 🚀 How to Run the Programs

Navigate to the `Week-3` directory in your terminal and run any script using Python 3:

```bash
cd Week-3
```

### Run Assignment 1 (Bank Account)
```bash
python bank_account.py
```

### Run Assignment 2 (Library Management System)
```bash
python library_system.py
```

### Run Assignment 3 (Calculator with Exception Handling)
```bash
python calculator.py
```

### Run Mini Project (Billing System)
```bash
python billing_system.py
```

---

## 💡 Example Usage & Output

### Billing System Output
```text
==============================================================
                      INVOICE / RECEIPT                       
==============================================================
 Customer Name : John Doe
 Tax Rate      : 8.5%
--------------------------------------------------------------
 #   | Product Name              | Price     | Qty  | Total     
--------------------------------------------------------------
 1   | Wireless Mouse            | $   25.99 |    2 | $    51.98
 2   | Mechanical Keyboard       | $   79.50 |    1 | $    79.50
 3   | USB-C Hub / Adapter       | $   19.99 |    3 | $    59.97
 4   | HDMI Cable (6ft)          | $    9.99 |    2 | $    19.98
--------------------------------------------------------------
                                      Subtotal : $   211.43
                                     Tax (8.5%) : $    17.97
==============================================================
                                   GRAND TOTAL : $   229.40
==============================================================
                 Thank you for your business!                 
```

---

## 🌟 Skills Demonstrated
- Class design, attribute initialization, and instance method development.
- Object composition and inter-class messaging.
- Robust exception handling (`try-except`) for safe program execution.
- Input validation and state integrity enforcement.
- Professional output formatting for CLI software.

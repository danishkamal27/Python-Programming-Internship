"""
Student Management System
-------------------------
A permanent CSV-backed student management system.
Week 2 Mini Project - Python Programming Internship
"""

import csv
import os

CSV_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")
FIELDNAMES = ["roll_number", "name", "marks"]


def load_students(filename=CSV_FILE):
    """
    Loads student data from a CSV file into a list of dictionaries.

    Returns:
        list: List of student dictionaries with keys 'roll_number', 'name', 'marks'.
    """
    students = []
    if not os.path.exists(filename):
        # If CSV file does not exist, initialize it with a header
        save_students(filename, students)
        return students

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure fields exist and marks can be float
                if "roll_number" in row and "name" in row and "marks" in row:
                    students.append({
                        "roll_number": row["roll_number"].strip(),
                        "name": row["name"].strip(),
                        "marks": float(row["marks"].strip())
                    })
    except Exception as e:
        print(f"Error loading student records from '{filename}': {e}")

    return students


def save_students(filename, students):
    """
    Saves the list of student dictionaries to a CSV file.

    Args:
        filename (str): Target CSV file path.
        students (list): List of student records.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for student in students:
                writer.writerow(student)
        return True
    except Exception as e:
        print(f"Error saving data to '{filename}': {e}")
        return False


def add_student(students, filename=CSV_FILE):
    """Adds a new student and saves immediately to CSV."""
    print("\n--- Add New Student ---")
    roll_number = input("Enter Roll Number: ").strip()
    if not roll_number:
        print("Error: Roll number cannot be empty.")
        return

    # Check for duplicate roll number
    for s in students:
        if s["roll_number"].lower() == roll_number.lower():
            print(f"Error: A student with Roll Number '{roll_number}' already exists.")
            return

    name = input("Enter Student Name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return

    marks_str = input("Enter Marks (0 - 100): ").strip()
    try:
        marks = float(marks_str)
        if marks < 0 or marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Marks must be a valid numeric value.")
        return

    new_student = {
        "roll_number": roll_number,
        "name": name,
        "marks": marks
    }

    students.append(new_student)
    if save_students(filename, students):
        print(f"Success: Student '{name}' (Roll: {roll_number}) added and saved to CSV!")


def search_student(students):
    """Searches for a student by roll number or name."""
    if not students:
        print("\nNo student records available.")
        return

    print("\n--- Search Student ---")
    query = input("Enter Roll Number or Name to search: ").strip()
    if not query:
        print("Error: Search query cannot be empty.")
        return

    found_students = [
        s for s in students
        if s["roll_number"].lower() == query.lower() or query.lower() in s["name"].lower()
    ]

    if found_students:
        print(f"\nFound {len(found_students)} matching record(s):")
        print(f"{'Roll No':<12} | {'Name':<25} | {'Marks':<8}")
        print("-" * 50)
        for s in found_students:
            print(f"{s['roll_number']:<12} | {s['name']:<25} | {s['marks']:<8.2f}")
        print("-" * 50)
    else:
        print(f"Error: No student found matching '{query}'.")


def delete_student(students, filename=CSV_FILE):
    """Deletes a student by roll number and updates CSV."""
    if not students:
        print("\nNo student records available to delete.")
        return

    print("\n--- Delete Student ---")
    roll_number = input("Enter Roll Number of student to delete: ").strip()
    if not roll_number:
        print("Error: Roll number cannot be empty.")
        return

    target_student = None
    for s in students:
        if s["roll_number"].lower() == roll_number.lower():
            target_student = s
            break

    if target_student:
        students.remove(target_student)
        if save_students(filename, students):
            print(f"Success: Student '{target_student['name']}' (Roll: {roll_number}) deleted and CSV updated!")
    else:
        print(f"Error: Student with Roll Number '{roll_number}' not found.")


def display_all_students(students):
    """Displays all student records."""
    if not students:
        print("\nNo student records found.")
        return

    print("\n=================== STUDENT RECORDS ===================")
    print(f"{'Roll No':<12} | {'Name':<25} | {'Marks':<8}")
    print("-" * 50)
    for s in students:
        print(f"{s['roll_number']:<12} | {s['name']:<25} | {s['marks']:<8.2f}")
    print("=======================================================")


def display_menu():
    """Displays menu options."""
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")


def main():
    """Main program execution loop."""
    filename = CSV_FILE
    students = load_students(filename)

    print("Welcome to Student Management System!")
    print(f"Loaded {len(students)} records from '{os.path.basename(filename)}'.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students, filename)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            delete_student(students, filename)
        elif choice == "4":
            display_all_students(students)
        elif choice == "5":
            print("Thank you for using Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 5.")


if __name__ == "__main__":
    main()

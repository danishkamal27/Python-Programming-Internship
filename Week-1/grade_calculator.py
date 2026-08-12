"""
Student Grade Calculator
Python Programming Internship - Week 1: Assignment 2

Calculates average marks and assigns letter grades based on student performance.
"""

def calculate_average(marks_list: list) -> float:
    """Calculate and return the average of a list of marks."""
    if not marks_list:
        return 0.0
    return sum(marks_list) / len(marks_list)


def determine_grade(average: float) -> str:
    """
    Determine letter grade based on average score.
    Grading Scale:
      90 - 100 : A
      80 - 89  : B
      70 - 79  : C
      60 - 69  : D
      Below 60 : F
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def get_valid_mark(subject_number: int) -> float:
    """Prompt the user for a valid mark between 0 and 100."""
    while True:
        try:
            mark_str = input(f"Enter mark for subject {subject_number} (0-100): ").strip()
            mark = float(mark_str)
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid range! Mark must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a numerical mark.")


def main():
    print("=" * 35)
    print("    Student Grade Calculator")
    print("=" * 35)

    while True:
        try:
            num_subjects_str = input("Enter number of subjects: ").strip()
            num_subjects = int(num_subjects_str)
            if num_subjects > 0:
                break
            else:
                print("Please enter a positive number of subjects.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    marks = []
    for i in range(1, num_subjects + 1):
        mark = get_valid_mark(i)
        marks.append(mark)

    avg = calculate_average(marks)
    grade = determine_grade(avg)

    print("\n" + "=" * 35)
    print("           RESULTS")
    print("=" * 35)
    print(f"Total Subjects : {num_subjects}")
    print(f"Total Marks    : {sum(marks):.2f} / {num_subjects * 100}")
    print(f"Average Score  : {avg:.2f}%")
    print(f"Final Grade    : {grade}")
    print("=" * 35)


if __name__ == "__main__":
    main()

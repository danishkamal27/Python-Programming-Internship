"""
Week 4 Capstone Project: Employee Data Analysis
Python Programming Internship

This program performs data analysis on employee dataset using Pandas library.
Key Features:
1. Load employee data from CSV file.
2. Calculate overall average salary and department-wise average salary.
3. Count total number of employees per department.
4. Filter employees earning above a specified salary threshold.
5. Export filtered dataset to a new CSV file.
"""

import os
import pandas as pd


def load_employee_data(file_path):
    """
    Loads employee data from a CSV file into a Pandas DataFrame.
    """
    print(f"\n--- 1. Loading Data from '{file_path}' ---")
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found!")
        return None

    df = pd.read_csv(file_path)
    print("Data loaded successfully!")
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    return df


def calculate_salary_metrics(df):
    """
    Calculates overall average salary and average salary by department.
    """
    print("\n--- 2. Salary Analysis ---")
    # Calculate overall average salary
    overall_avg_salary = df["Salary"].mean()
    print(f"Overall Average Salary: ${overall_avg_salary:,.2f}")

    # Calculate average salary grouped by department
    print("\nAverage Salary by Department:")
    dept_avg_salary = df.groupby("Department")["Salary"].mean().round(2)
    for dept, avg_sal in dept_avg_salary.items():
        print(f"  - {dept}: ${avg_sal:,.2f}")

    return overall_avg_salary, dept_avg_salary


def count_employees_by_department(df):
    """
    Counts total number of employees in each department.
    """
    print("\n--- 3. Employee Count by Department ---")
    dept_counts = df["Department"].value_counts()
    for dept, count in dept_counts.items():
        print(f"  - {dept}: {count} employee(s)")
    return dept_counts


def filter_employees_by_salary(df, threshold=75000):
    """
    Filters employees earning strictly more than the specified salary threshold.
    """
    print(f"\n--- 4. Filtering Employees (Salary > ${threshold:,.2f}) ---")
    filtered_df = df[df["Salary"] > threshold]
    print(f"Found {len(filtered_df)} employee(s) matching the criteria:")
    print(filtered_df[["EmployeeID", "Name", "Department", "Salary"]])
    return filtered_df


def export_data_to_csv(df, output_path):
    """
    Exports a DataFrame to a CSV file.
    """
    print(f"\n--- 5. Exporting Results to '{output_path}' ---")
    df.to_csv(output_path, index=False)
    print(f"Successfully saved filtered data to '{output_path}'.")


def main():
    print("==================================================")
    print("        EMPLOYEE DATA ANALYSIS PROGRAM            ")
    print("==================================================")

    # File paths relative to Week-4 directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(script_dir, "employees.csv")
    output_csv = os.path.join(script_dir, "high_salary_employees.csv")

    # Step 1: Load Data
    df = load_employee_data(input_csv)
    if df is None:
        return

    # Step 2: Calculate Salary Metrics
    calculate_salary_metrics(df)

    # Step 3: Count Employees by Department
    count_employees_by_department(df)

    # Step 4: Filter High Earners (Default threshold: $75,000)
    salary_threshold = 75000
    filtered_df = filter_employees_by_salary(df, threshold=salary_threshold)

    # Step 5: Export Filtered Data to CSV
    export_data_to_csv(filtered_df, output_csv)

    print("\n==================================================")
    print("          ANALYSIS COMPLETED SUCCESSFULLY          ")
    print("==================================================")


if __name__ == "__main__":
    main()

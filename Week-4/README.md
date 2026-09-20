# Week 4 — Capstone Project: Employee Data Analysis

Welcome to **Week 4** of the Python Programming Internship repository! This capstone project focuses on data analysis and manipulation using the powerful **Pandas** library in Python.

---

## 📚 Topics & Concepts Covered
- **Data Loading**: Reading CSV files into Pandas `DataFrame` structures (`pd.read_csv`).
- **Data Summary & Overview**: Inspecting dataset dimensions, headers, and preview rows (`df.head()`).
- **Statistical Aggregation**: Calculating overall dataset averages and summary statistics (`mean()`).
- **Data Grouping & Aggregation**: Grouping records by categorical fields (`groupby()`) to compute department-level metrics.
- **Categorical Frequency Counting**: Aggregating headcount distributions (`value_counts()`).
- **Boolean Masking & Data Filtering**: Selecting subsets of data based on quantitative conditional criteria (`df[df['Salary'] > threshold]`).
- **Data Exporting**: Writing processed and filtered DataFrame results back to CSV files (`to_csv()`).

---

## 📁 Week 4 Directory Structure

```text
Week-4/
├── README.md                   # Project documentation & execution instructions
├── employees.csv               # Sample dataset containing employee records
├── employee_analysis.py        # Main Python script for data analysis with Pandas
└── high_salary_employees.csv   # Exported dataset containing employees above salary threshold
```

---

## 📋 Assignment Requirements & Implementation

### Capstone Project: Employee Data Analysis (`employee_analysis.py`)
- **Description**: An automated data analysis script that processes employee records from a CSV file, computes key salary metrics, measures department headcounts, filters high-earning staff, and exports results.
- **Key Features**:
  1. **Load Employee Data**: Uses Pandas to safely load `employees.csv`.
  2. **Calculate Average Salary**: Computes overall average salary across all employees as well as department-level average salaries.
  3. **Count Employees by Department**: Aggregates employee counts per department.
  4. **Filter Employees**: Identifies employees earning above a customizable salary threshold (default: `$75,000`).
  5. **Export Results**: Writes the filtered list of high-earning employees to `high_salary_employees.csv`.

---

## 💻 Requirements & Prerequisites

- Python 3.8 or higher installed on your system.
- `pandas` library installed:
  ```bash
  pip install pandas
  ```

---

## 🚀 How to Run the Program

1. Open your Command Prompt (Windows) or Terminal.
2. Navigate to the `Week-4` directory:
   ```cmd
   cd Python-Programming-Internship\Week-4
   ```
3. Execute the Python script:
   ```cmd
   python employee_analysis.py
   ```

---

## 📊 Sample Program Output

```text
==================================================
        EMPLOYEE DATA ANALYSIS PROGRAM            
==================================================

--- 1. Loading Data from 'C:\...\Week-4\employees.csv' ---
Data loaded successfully!

First 5 rows of the dataset:
   EmployeeID            Name         Department  Salary  Age    JoinDate
0         101   Alice Johnson        Engineering   85000   30  2021-03-15
1         102      Bob Smith              Sales   62000   28  2022-01-10
2         103  Charlie Brown        Engineering   92000   35  2019-11-01
3         104    Diana Prince    Human Resources   58000   32  2020-05-20
4         105    Evan Wright              Sales   71000   29  2021-08-12

--- 2. Salary Analysis ---
Overall Average Salary: $77,866.67

Average Salary by Department:
  - Engineering: $87,750.00
  - Finance: $85,250.00
  - Human Resources: $59,500.00
  - Marketing: $69,000.00
  - Sales: $67,000.00

--- 3. Employee Count by Department ---
  - Engineering: 4 employee(s)
  - Finance: 4 employee(s)
  - Sales: 3 employee(s)
  - Human Resources: 2 employee(s)
  - Marketing: 2 employee(s)

--- 4. Filtering Employees (Salary > $75,000.00) ---
Found 9 employee(s) matching the criteria:
    EmployeeID            Name   Department  Salary
0          101   Alice Johnson  Engineering   85000
2          103   Charlie Brown  Engineering   92000
6          107    George Clark  Engineering   78000
7          108   Hannah Abbott      Finance   89000
8          109     Ian Malcolm      Finance   94000
11         112     Laura Croft  Engineering   96000
13         114   Nina Williams      Finance   82000
14         115  Oscar Martinez      Finance   76000

--- 5. Exporting Results to 'C:\...\Week-4\high_salary_employees.csv' ---
Successfully saved filtered data to 'C:\...\Week-4\high_salary_employees.csv'.

==================================================
          ANALYSIS COMPLETED SUCCESSFULLY          
==================================================
```

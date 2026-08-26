# Week 2 — Data Structures, File I/O & Exception Handling

Welcome to **Week 2** of the Python Programming Internship repository! This week focuses on mastering core Python data structures, reading and writing files (Text, CSV, JSON), and implementing robust exception handling.

---

## 📚 Topics Covered
- **Data Structures**: Lists, Tuples, Sets, Dictionaries
- **File Handling**: Reading & writing text files using `with open(...)`
- **CSV Data**: Structured CSV parsing & persistence using the `csv` module
- **JSON Data**: Serialization & deserialization using the built-in `json` module
- **Exception Handling**: Graceful error management using `try-except` blocks

---

## 📁 Week 2 Directory Structure

```text
Week-2/
├── README.md                     # Documentation for Week 2
├── contact_book.py               # Assignment 1: Dictionary-based Contact Book
├── word_counter.py               # Assignment 2: Text file word, line & char counter
├── sample_text.txt               # Sample input text file for Assignment 2
├── json_file_reader.py           # Assignment 3: JSON Reader & formatted display
├── sample_data.json              # Sample input JSON file for Assignment 3
├── student_management_system.py  # Mini Project: CSV-backed Student Management System
└── students.csv                  # Persistent CSV storage file for Mini Project
```

---

## 📋 Assignment Summaries & Features

### 1. Contact Book (`contact_book.py`)
- **Description**: An interactive CLI contact management program.
- **Key Features**:
  - Main data structure: Python nested dictionary (`{name: {"phone": ..., "email": ...}}`).
  - Modular operations: Add, Search, Update, Delete, View All.
  - Input validation and graceful handling for non-existent contacts or invalid menu options.

### 2. Word Counter (`word_counter.py` & `sample_text.txt`)
- **Description**: Analyzes text files and calculates structural metrics.
- **Key Features**:
  - Counts lines, words, and total characters.
  - Safe file opening using `with open(..., 'r', encoding='utf-8')`.
  - Gracefully handles missing files (`FileNotFoundError`).

### 3. JSON File Reader (`json_file_reader.py` & `sample_data.json`)
- **Description**: Reads and displays formatted JSON files.
- **Key Features**:
  - Parses JSON content using the built-in `json` module.
  - Pretty-prints output using `json.dumps(..., indent=4)`.
  - Handles `FileNotFoundError` and `json.JSONDecodeError` for malformed JSON.

### 4. Mini Project: Student Management System (`student_management_system.py` & `students.csv`)
- **Description**: A persistent Student Management System using a CSV database.
- **Key Features**:
  - Fields: `roll_number`, `name`, `marks`.
  - Full CRUD operations: Add student, Search student, Delete student, Display all.
  - Automatic CSV synchronization on every change.
  - Duplicate roll number detection and numerical marks validation (0-100).
  - Data remains intact across program restarts.

---

## 🚀 How to Run the Programs

Run each script directly from the terminal inside the `Week-2` directory:

### Run Assignment 1 (Contact Book)
```bash
python contact_book.py
```

### Run Assignment 2 (Word Counter)
```bash
python word_counter.py
```

### Run Assignment 3 (JSON Reader)
```bash
python json_file_reader.py
```

### Run Mini Project (Student Management System)
```bash
python student_management_system.py
```

---

## 💡 Example Usage & Output

### Word Counter Output
```text
================ Text File Analysis ================
 File Analyzed     : sample_text.txt
 Total Lines       : 5
 Total Words       : 42
 Total Characters  : 301
====================================================
```

### Student Management System Output
```text
=================== STUDENT RECORDS ===================
Roll No      | Name                      | Marks   
--------------------------------------------------
101          | Alice Johnson             | 88.50   
102          | Bob Smith                 | 92.00   
103          | Charlie Brown             | 76.00   
=======================================================
```

---

## 🌟 Skills Demonstrated
- Advanced usage of Python dictionaries and list comprehensions.
- File I/O operations with UTF-8 encoding support.
- Parsing and writing CSV and JSON formats using native standard libraries.
- Defensive programming with input validation and exception handling.
- Modular code architecture with clean function organization and `if __name__ == "__main__":` entry points.

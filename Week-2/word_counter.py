"""
Word Counter Tool
-----------------
A beginner-friendly tool to count lines, words, and characters in a text file.
Week 2 - Python Programming Internship
"""

import os


def analyze_text_file(filename):
    """
    Reads a text file and returns line, word, and character counts.

    Args:
        filename (str): Path to the text file.

    Returns:
        tuple or None: (lines, words, characters) if successful, None if error occurs.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Count lines
            # Splitlines handles different line ending types (\n, \r\n) cleanly
            lines = len(content.splitlines()) if content else 0
            
            # Count words
            words = len(content.split())
            
            # Count total characters (including whitespace)
            characters = len(content)

            return lines, words, characters

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None


def display_results(filename, counts):
    """Print the text analysis results in a structured format."""
    if counts is None:
        return

    lines, words, characters = counts
    print("\n================ Text File Analysis ================")
    print(f" File Analyzed     : {filename}")
    print(f" Total Lines       : {lines}")
    print(f" Total Words       : {words}")
    print(f" Total Characters  : {characters}")
    print("====================================================")


def main():
    """Main program execution."""
    default_filename = "sample_text.txt"

    # Determine default file location relative to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, default_filename)

    print("--- WORD COUNTER TOOL ---")
    user_input = input(f"Enter file path to analyze (Press Enter for '{default_filename}'): ").strip()

    if user_input:
        file_path = user_input

    counts = analyze_text_file(file_path)
    display_results(file_path, counts)


if __name__ == "__main__":
    main()

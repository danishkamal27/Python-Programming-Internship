"""
JSON File Reader
----------------
A Python program to load, parse, and display JSON files cleanly with exception handling.
Week 2 - Python Programming Internship
"""

import json
import os


def load_json_file(filename):
    """
    Reads and parses a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        dict or list or None: Parsed JSON content if successful, None otherwise.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print(f"Error: The JSON file '{filename}' was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        print(f"Details: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None


def display_formatted_json(data):
    """
    Prints JSON data in a pretty, human-readable format.

    Args:
        data (dict or list): Python data structure parsed from JSON.
    """
    if data is None:
        return

    print("\n================ Formatted JSON Output ================")
    # Using built-in json.dumps with indent=4 for clean formatting
    formatted_str = json.dumps(data, indent=4)
    print(formatted_str)
    print("=======================================================")


def main():
    """Main program execution."""
    default_filename = "sample_data.json"

    # Locate sample_data.json in the same directory as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, default_filename)

    print("--- JSON FILE READER ---")
    user_input = input(f"Enter JSON file path to read (Press Enter for '{default_filename}'): ").strip()

    if user_input:
        file_path = user_input

    data = load_json_file(file_path)
    if data is not None:
        print(f"\nSuccess: Successfully loaded and parsed '{file_path}'.")
        display_formatted_json(data)


if __name__ == "__main__":
    main()

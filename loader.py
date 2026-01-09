

import csv
import os

# Global variable to store the file path for reuse in Task B
csv_file_path = None


def prompt_file_path():
    """
    Prompt user to input CSV file path or use default.
    
    Returns:
        str: The file path entered by user or default path
    """
    default_path = "Urban_wildlife.csv"
    print("\n=== CSV File Loader ===")
    user_input = input(f"Enter CSV file path (or press Enter for default '{default_path}'): ").strip()
    
    if user_input == "":
        return default_path
    return user_input


def validate_csv_file(file_path):
    """
    Validate that the CSV file exists and has expected number of columns.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        tuple: (is_valid, error_message)
    """
    # Check if file exists
    if not os.path.exists(file_path):
        return False, f"Error: File '{file_path}' does not exist."
    
    # Check if file has correct number of columns
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            
            if len(header) != 23:  # Expected 23 columns
                return False, f"Error: Expected 23 columns, found {len(header)} columns."
                
        return True, "File validated successfully."
    
    except Exception as e:
        return False, f"Error reading file: {str(e)}"


def load_csv_as_list(file_path):
    """
    Load CSV file using csv.reader() into a list of rows.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        tuple: (header_row, data_rows) where header_row is list and data_rows is list of lists
    """
    global csv_file_path
    csv_file_path = file_path  # Store for Task B reuse
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header_row = next(csv_reader)
            data_rows = list(csv_reader)
            
        print(f"\n✓ Successfully loaded {len(data_rows)} records from CSV file.")
        print(f"✓ Columns: {len(header_row)}")
        
        return header_row, data_rows
    
    except Exception as e:
        print(f"Error loading CSV: {str(e)}")
        return None, None


def get_csv_file_path():
    """
    Returns the stored CSV file path for reuse in Task B.
    
    Returns:
        str: The stored CSV file path
    """
    return csv_file_path


def initialize_data():
    """
    Complete data initialization workflow.
    Prompts for file, validates, and loads data.
    
    Returns:
        tuple: (header_row, data_rows, file_path) or (None, None, None) on failure
    """
    file_path = prompt_file_path()
    
    # Validate file
    is_valid, message = validate_csv_file(file_path)
    print(message)
    
    if not is_valid:
        return None, None, None
    
    # Load data
    header_row, data_rows = load_csv_as_list(file_path)
    
    if header_row is None:
        return None, None, None
    
    return header_row, data_rows, file_path

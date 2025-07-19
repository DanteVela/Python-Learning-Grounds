# A simple Python script to create an Excel file using pandas.
# This script demonstrates how to create an Excel file with sample data.
# --------------------------------------------------------------------------------------------------------------------------------

# Import necessary libraries
import pandas as pd
import openpyxl                 # Ensure openpyxl is installed for Excel file handling

# Sample Data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

# Create pandas DataFrame
df = pd.DataFrame(data)

# Define File Path
file_path = 'SampleData.xlsx'

# Get user input for file path
file_path = input("Enter the file path to save the Excel file (default is 'SampleData.xlsx'): ") or file_path
file_path = file_path.strip()  # Ensure no leading/trailing spaces

# Ensure the file path is valid
if not file_path.endswith('.xlsx'):
    raise ValueError("File path must end with '.xlsx'")

# Write DataFrame to Excel File
df.to_excel(file_path, index=False)

# Notify user of successful creation
print(f"Excel file '{file_path}' created successfully with the sample data.")
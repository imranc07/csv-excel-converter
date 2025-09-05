"""
📌 Problem Statement:
Create a Python script that can read data from a CSV file and write it to an Excel file (and vice versa).
"""

import pandas as pd

# ✅ Define file paths (use raw string or double backslashes for Windows paths)
csv_file = r"Path of data.csv file"
excel_file = "data_output.xlsx"

# 🔹 Step 1: Read data from CSV
csv_data = pd.read_csv(csv_file)

# 🖨️ Print original CSV content
print("CSV Data (Original):")
print(csv_data)

# 🔹 Step 2: Create new rows to append
new_rows = pd.DataFrame({
    'Name': [
        'Rahul', 'Anjali', 'Pooja', 'Karan', 'Simran',
        'Rohan', 'Meera', 'Deepak', 'Sunita', 'Arnav'
    ],
    'Age': [
        29, 27, 28, 34, 29,
        32, 27, 31, 26, 30
    ],
    'City': [
        'Bangalore', 'Delhi', 'Hyderabad', 'Kolkata', 'Ahmedabad',
        'Jaipur', 'Lucknow', 'Chandigarh', 'Indore', 'Surat'
    ],
    'Department': [
        'IT', 'HR', 'Finance', 'Marketing', 'Sales',
        'Operations', 'IT', 'HR', 'Finance', 'Sales'
    ],
    'Salary': [
        59000, 52000, 60000, 53000, 58000,
        57000, 54000, 61000, 48000, 55000
    ]
})

# 🔹 Step 3: Append new rows to existing CSV data
updated_data = pd.concat([csv_data, new_rows], ignore_index=True)

# 🖨️ Print updated dataset after appending new rows
print("\nData After Appending New Rows:")
print(updated_data)

# 🔹 Step 4: Write updated data to Excel file (without overwriting original CSV)
updated_data.to_excel(excel_file, index=False)

# 🔹 Step 5: Read back data from Excel to verify
excel_data = pd.read_excel(excel_file)

# 🖨️ Print Excel content after writing
print("\nExcel Data Read Back (Final Output):")
print(excel_data)

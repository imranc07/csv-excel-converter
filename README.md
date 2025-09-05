# CSV to Excel Converter using Python 🐍

## 📌 Problem Statement
Create a Python script that can read data from a CSV file and write it to an Excel file (and vice versa).

## 🚀 Features
- Read data from a CSV file using **pandas**
- Append new rows of data
- Write the updated data into an **Excel file**
- Read back from Excel for verification
- Keeps the original CSV file intact

## 🛠️ Technologies Used
- Python 3
- pandas library
- openpyxl (Excel support)

## 📂 File Structure
```
csv_excel_converter/
│── data.csv                   # Input CSV file
│── data_output.xlsx           # Output Excel file (auto-generated)
│── CSV_Excel_Read_&_Write.py  # Python script
│── README.md                  # Documentation
```

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install pandas openpyxl
   ```

2. Run the script:
   ```bash
   python script.py
   ```

3. Check the output in `data_output.xlsx`.

## 📊 Example Workflow
1. Read `data.csv` → Display original data  
2. Append new rows → Display updated data  
3. Write to `data_output.xlsx`  
4. Read back from Excel → Verify final data  

## ✨ Author
👨‍💻 Imran Ahmad  
*Python Automation Tester | Selenium | PyTest | API Testing | CI/CD | POM | DDT & KDT | Robot Framework*

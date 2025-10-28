import pandas as pd
import os

def inspect_sheets(folder):
    files = os.listdir(folder)
    for file in files:
        if file.endswith(".xlsx"):
            filepath = os.path.join(folder, file)
            try:
                xls = pd.ExcelFile(filepath)
                print(f"File: {file}")
                print(f"Sheet names: {xls.sheet_names}")
                print("-" * 20)
            except Exception as e:
                print(f"Could not read {file}: {e}")

if __name__ == '__main__':
    inspect_sheets("downloaded_excel")

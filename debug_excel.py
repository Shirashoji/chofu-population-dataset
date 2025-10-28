import pandas as pd

def debug_excel(filepath):
    xls = pd.ExcelFile(filepath)
    sheet_name = xls.sheet_names[-1]
    print(f"Reading sheet: {sheet_name}")

    df = pd.read_excel(xls, sheet_name=sheet_name, header=None)
    print("First 10 rows:")
    print(df.head(10))

    print("\nDataFrame Info:")
    df_with_header = pd.read_excel(xls, sheet_name=sheet_name, header=1, skiprows=[2])
    print(df_with_header.info())
    print("\nColumns:")
    print(df_with_header.columns)

if __name__ == '__main__':
    debug_excel("downloaded_excel_new/r5chouchoubetu.xlsx")

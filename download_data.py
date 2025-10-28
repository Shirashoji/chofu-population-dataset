import requests
import pandas as pd
import os

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = url.split('/')[-1]
    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        print(f"Downloading {filename}...")
        response = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print(f"{filename} already exists.")
    return filepath

def convert_excel_to_csv(excel_path, csv_path):
    print(f"Converting {excel_path} to CSV...")
    xls = pd.ExcelFile(excel_path)
    # The target sheet is the last one
    target_sheet = xls.sheet_names[-1]

    # Now read the correct sheet with the header
    df = pd.read_excel(xls, sheet_name=target_sheet, header=4) # Assuming header is on the 5th row (index 4)

    # Drop unnecessary rows and columns
    df = df.iloc[1:, :]
    df = df.drop(df.columns[[1, 2]], axis=1)

    # Rename columns to match the existing CSV format
    df.columns = [
        '町丁', '全世代（男）', '全世代（女）',
        '0～4歳（男）', '0～4歳（女）', '5～9歳（男）', '5～9歳（女）',
        '10～14歳（男）', '10～14歳（女）', '15～19歳（男）', '15～19歳（女）',
        '20～24歳（男）', '20～24歳（女）', '25～29歳（男）', '25～29歳（女）',
        '30～34歳（男）', '30～34歳（女）', '35～39歳（男）', '35～39歳（女）',
        '40～44歳（男）', '40～44歳（女）', '45～49歳（男）', '45～49歳（女）',
        '50～54歳（男）', '50～54歳（女）', '55～59歳（男）', '55～59歳（女）',
        '60～64歳（男）', '60～64歳（女）', '65～69歳（男）', '65～69歳（女）',
        '70～74歳（男）', '70～74歳（女）', '75～79歳（男）', '75～79歳（女）',
        '80～84歳（男）', '80～84歳（女）', '85～89歳（男）', '85～89歳（女）',
        '90～94歳（男）', '90～94歳（女）', '95～99歳（男）', '95～99歳（女）',
        '100歳以上（男）', '100歳以上（女）', '総数'
    ]

    df.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"Converted to {csv_path}")

if __name__ == '__main__':
    urls = {
        "2022": "https://www.city.chofu.lg.jp/documents/4693/r4chouchoubetsu.xlsx",
        "2023": "https://www.city.chofu.lg.jp/documents/4693/r5chouchoubetu.xlsx",
        "2024": "https://www.city.chofu.lg.jp/documents/4693/r6chouchobetu.xlsx"
    }

    download_folder = "downloaded_excel"
    csv_folder = "csvData"

    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    for year, url in urls.items():
        excel_path = download_file(url, download_folder)
        csv_path = os.path.join(csv_folder, f"{year}.csv")
        convert_excel_to_csv(excel_path, csv_path)

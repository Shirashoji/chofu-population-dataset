import requests
import pandas as pd
import os

def download_file(url, folder):
    """指定されたURLからファイルをダウンロードする"""
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

def process_new_format_excel(excel_path, csv_path):
    """新しい形式のExcelファイルを処理してCSVに変換する"""
    print(f"Processing {excel_path}...")
    try:
        xls = pd.ExcelFile(excel_path)
        # 最後のシートを対象とする
        target_sheet = xls.sheet_names[-1]

        # ヘッダーは2行目(index=1)と3行目(index=2)をスキップしてデータを読み込む
        df = pd.read_excel(xls, sheet_name=target_sheet, header=1, skiprows=[2])

        # r4chouchoubetsu.xlsx の場合のみ、不要な列を削除
        if 'r4chouchoubetsu' in excel_path:
            df = df.drop(df.columns[1], axis=1)

        # 列名をリネーム
        df.columns = ['町丁', '男性', '女性', '総人口', '世帯数']

        # '計' や '合計' を含む行（集計行）を削除
        df = df[~df['町丁'].astype(str).str.contains('計')]

        # '総数' を含む行を削除
        df = df[~df['町丁'].astype(str).str.contains('総数')]

        # 空白の町丁名の行を削除
        df.dropna(subset=['町丁'], inplace=True)

        # ファイルに保存
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Successfully converted to {csv_path}")

    except Exception as e:
        print(f"Error processing {excel_path}: {e}")

if __name__ == '__main__':
    urls = {
        "2022": "https://www.city.chofu.lg.jp/documents/4693/r4chouchoubetsu.xlsx",
        "2023": "https://www.city.chofu.lg.jp/documents/4693/r5chouchoubetu.xlsx",
        "2024": "https://www.city.chofu.lg.jp/documents/4693/r6chouchobetu.xlsx"
    }

    download_folder = "downloaded_excel_new"
    csv_folder = "csvData_new"

    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    for year, url in urls.items():
        excel_path = download_file(url, download_folder)
        csv_path = os.path.join(csv_folder, f"{year}_new.csv")
        process_new_format_excel(excel_path, csv_path)

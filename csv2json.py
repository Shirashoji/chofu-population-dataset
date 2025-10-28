import csv
import json
import os

def csv2json(csvFilePath, jsonFilePath, encoding="utf-8"):
    # Open the CSV
    with open(csvFilePath, 'r', encoding=encoding) as f:
        dr = csv.DictReader(f)
        data = [row for row in dr]

    # Write the JSON
    with open(jsonFilePath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
    for file in files:
        csv_path = os.path.join(input_dir, file)
        json_path = os.path.join(output_dir, file.replace('.csv', '.json'))
        print(f"Converting {csv_path} to {json_path}")
        csv2json(csv_path, json_path)

if __name__ == '__main__':
    # 既存のデータを処理
    process_directory("./csvData", "./rawJSON")
    # 新しいデータを処理
    process_directory("./csvData_new", "./rawJSON_new")

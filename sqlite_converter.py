import sqlite3
import csv
import sys


def sqlite_to_csv(db_file, table_name, csv_file):
    # SQLiteデータベースに接続
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # テーブルの全データを取得
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    rows = [[str(col).replace('ー', '-') for col in row] for row in rows]

    # カラム名を取得
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    # CSVファイルに書き込み
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(columns)  # ヘッダーを書き込み
        csvwriter.writerows(rows)    # データを書き込み

    # 接続を閉じる
    conn.close()

    print(f"{csv_file} にデータを書き込みました。")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("使用方法: python script.py <データベースファイル> <テーブル名> <出力CSVファイル>")
        sys.exit(1)

    db_file = sys.argv[1]
    table_name = sys.argv[2]
    csv_file = sys.argv[3]

    sqlite_to_csv(db_file, table_name, csv_file)

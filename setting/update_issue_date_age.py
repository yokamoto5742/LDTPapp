import os
import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# アプリケーションのディレクトリを設定
if getattr(sys, 'frozen', False):
    app_directory = r"C:\Shinseikai\LDTPapp"
    os.chdir(app_directory)

# configパーサーをインポートし、設定を読み込む
import configparser
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
db_url = config.get('Database', 'db_url')

# SQLAlchemyの設定
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)

# PatientInfoモデルをインポート（アプリケーションのメインファイルから）
from main import PatientInfo

@contextmanager
def session_scope():
    """セッションのコンテキストマネージャー"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"エラーが発生しました: {e}")
        raise
    finally:
        session.close()

def calculate_issue_date_age(birth_date, issue_date):
    """発行日時点の年齢を計算する関数"""
    issue_date_age = issue_date.year - birth_date.year
    if issue_date.month < birth_date.month or (
            issue_date.month == birth_date.month and issue_date.day < birth_date.day):
        issue_date_age -= 1
    return issue_date_age

def update_issue_date_age():
    """既存のデータに対してissue_date_ageを計算し更新する"""
    with session_scope() as session:
        patients = session.query(PatientInfo).all()
        total = len(patients)
        updated = 0
        for i, patient in enumerate(patients, 1):
            try:
                patient.issue_date_age = calculate_issue_date_age(patient.birthdate, patient.issue_date)
                updated += 1
                if i % 100 == 0:  # 100レコードごとに進捗を表示
                    print(f"進捗: {i}/{total} レコードを処理しました")
            except Exception as e:
                print(f"ID {patient.id} の更新中にエラーが発生しました: {e}")
        
        print(f"\n更新完了: {updated}/{total} レコードが正常に更新されました")

if __name__ == "__main__":
    print("既存データの issue_date_age フィールドを更新します")
    update_issue_date_age()
    print("処理が完了しました")

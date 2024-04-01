import flet as ft
import sqlite3
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook

conn = None
c = None

def init_db():
    global conn, c
    conn = sqlite3.connect("ldtp_app.db", check_same_thread=False)
    c = conn.cursor()

    # 療養計画書テーブルを作成
    c.execute("""
        CREATE TABLE IF NOT EXISTS treatment_plans (
            id INTEGER PRIMARY KEY,
            patient_id INTEGER,
            issue_date TEXT,
            doctor_id INTEGER,
            department TEXT,
            creation_count INTEGER,
            main_disease TEXT,
            sheet_name TEXT,
            weight REAL
        )
    """)
    conn.commit()

    # 主病名テーブルを作成
    c.execute("""
        CREATE TABLE IF NOT EXISTS main_diseases (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    conn.commit()

    # シート名テーブルを作成
    c.execute("""
        CREATE TABLE IF NOT EXISTS sheet_names (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)
    conn.commit()

    # 主病名の初期データを挿入
    c.execute("INSERT OR IGNORE INTO main_diseases (name) VALUES (?)", ("高血圧",))
    c.execute("INSERT OR IGNORE INTO main_diseases (name) VALUES (?)", ("脂質異常症",))
    c.execute("INSERT OR IGNORE INTO main_diseases (name) VALUES (?)", ("糖尿病",))
    conn.commit()

    # シート名の初期データを挿入
    c.execute("INSERT OR IGNORE INTO sheet_names (name) VALUES (?)", ("DM01",))
    c.execute("INSERT OR IGNORE INTO sheet_names (name) VALUES (?)", ("DM02",))
    c.execute("INSERT OR IGNORE INTO sheet_names (name) VALUES (?)", ("DM03",))
    conn.commit()

def load_patient_data():
    return pd.read_csv("C:\\InnoKarte\\pat.csv", encoding="shift_jis")

def create_treatment_plan(patient_id, doctor_id, department, creation_count, main_disease, sheet_name, weight, df_patients):
    global c, conn
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    workbook = load_workbook("C:\\Shinseikai\\LDTPapp\\生活習慣病療養計画書.xlsm")
    common_sheet = workbook["共通情報"]
    patient_info = df_patients[df_patients["患者ID"] == patient_id].iloc[0]

    common_sheet["B2"] = patient_info["患者ID"]
    common_sheet["B3"] = patient_info["氏名"]
    common_sheet["B4"] = patient_info["カナ"]
    common_sheet["B5"] = "男性" if patient_info["性別　1:男性　2:女性"] == 1 else "女性"
    common_sheet["B6"] = patient_info["生年月日"]
    common_sheet["B8"] = creation_count
    common_sheet["C11"] = datetime.now().strftime("%Y/%m/%d")
    common_sheet["C12"] = doctor_id
    common_sheet["C13"] = patient_info["医師名"]
    common_sheet["C14"] = department
    common_sheet["C15"] = creation_count
    common_sheet["C16"] = main_disease
    common_sheet["C17"] = sheet_name
    common_sheet["C18"] = weight

    selected_sheet = workbook[sheet_name]

    new_file_name = f"生活習慣病療養計画書_{current_datetime}.xlsm"
    workbook.save(f"C:\\Shinseikai\\LDTPapp\\{new_file_name}")

    c.execute("""
        INSERT INTO treatment_plans (patient_id, issue_date, doctor_id, department, creation_count, main_disease, sheet_name, weight)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (patient_id, datetime.now().strftime("%Y-%m-%d"), doctor_id, department, creation_count, main_disease,
          sheet_name, weight))
    conn.commit()

def get_issued_plans():
    global c
    c.execute("SELECT * FROM treatment_plans")
    return c.fetchall()

def load_main_diseases():
    global c
    c.execute("SELECT name FROM main_diseases")
    return [ft.dropdown.Option(row[0]) for row in c.fetchall()]

def load_sheet_names():
    global c
    c.execute("SELECT name FROM sheet_names")
    return [ft.dropdown.Option(row[0]) for row in c.fetchall()]

async def main_async(page: ft.Page, df_patients: pd.DataFrame):
    page.title = "生活習慣病療養計画書アプリ"
    init_db()

    def load_patient_info(patient_id):
        patient_info = df_patients[df_patients["患者ID"] == patient_id].iloc[0]
        name_value.value = patient_info["氏名"]
        kana_value.value = patient_info["カナ"]
        gender_value.value = "男性" if patient_info["性別　1:男性　2:女性"] == 1 else "女性"
        birthdate_value.value = patient_info["生年月日"]
        doctor_name_value.value = patient_info["医師名"]
        name_value.update()
        kana_value.update()
        gender_value.update()
        birthdate_value.update()
        doctor_name_value.update()

    def create_new_plan(e):
        patient_id = int(patient_id_value.value)
        doctor_id = int(doctor_id_value.value)
        department = department_value.value
        creation_count = int(creation_count_value.value)
        main_disease = main_disease_dropdown.value
        sheet_name = sheet_name_dropdown.value
        weight = float(weight_value.value)

        create_treatment_plan(patient_id, doctor_id, department, creation_count, main_disease, sheet_name, weight, df_patients)
        page.snack_bar = ft.SnackBar(content=ft.Text("療養計画書が作成されました"))
        page.snack_bar.open = True
        page.update()

    def view_issued_plans(e):
        issued_plans = get_issued_plans()
        plans_text = "\n".join([
                                   f"発行日: {str(plan[2])}, 診療科: {str(plan[4])}, 医師名: {str(plan[3])}, 主病名: {str(plan[6])}, シート名: {str(plan[7])}, 作成回数: {str(plan[5])}"
                                   for plan in issued_plans])
        issued_plans_textfield.value = plans_text
        issued_plans_textfield.update()

    def print_plan(e):
        pass

    def delete_plan(e):
        pass

    def close_dialog(e):
        dialog.open = False
        page.update()

    def on_patient_id_change(e):
        patient_id = int(patient_id_value.value)
        load_patient_info(patient_id)

    patient_id_value = ft.TextField(label="患者ID", on_change=on_patient_id_change)
    name_value = ft.TextField(label="氏名", read_only=True)
    kana_value = ft.TextField(label="カナ", read_only=True)
    gender_value = ft.TextField(label="性別", read_only=True)
    birthdate_value = ft.TextField(label="生年月日", read_only=True)

    main_disease_options = load_main_diseases()
    sheet_name_options = load_sheet_names()

    doctor_id_value = ft.TextField(label="医師ID")
    doctor_name_value = ft.TextField(label="医師名", read_only=True)
    department_value = ft.TextField(label="診療科")
    creation_count_value = ft.TextField(label="作成回数")
    main_disease_dropdown = ft.Dropdown(label="主病名", options=main_disease_options)
    sheet_name_dropdown = ft.Dropdown(label="シート名", options=sheet_name_options)
    weight_value = ft.TextField(label="体重")

    create_button = ft.ElevatedButton("登録", on_click=create_new_plan)
    print_button = ft.ElevatedButton("印刷", on_click=print_plan)
    delete_button = ft.ElevatedButton("削除", on_click=delete_plan)
    close_button = ft.ElevatedButton("閉じる", on_click=close_dialog)

    issued_plans_textfield = ft.TextField(multiline=True, read_only=True)
    view_issued_button = ft.ElevatedButton("発行履歴", on_click=view_issued_plans)

    dialog = ft.AlertDialog(
        title=ft.Text("医師記入欄"),
        content=ft.Column([
            ft.Text("発行日"),
            doctor_id_value,
            doctor_name_value,
            department_value,
            creation_count_value,
            main_disease_dropdown,
            sheet_name_dropdown,
            weight_value
        ]),
        actions=[
            create_button,
            print_button,
            delete_button,
            close_button
        ],
    )

    page.add(
        ft.Text("生活習慣病療養計画書", size=20),
        ft.Row([
            ft.Column([
                patient_id_value,
                name_value,
                kana_value,
                gender_value,
                birthdate_value
            ]),
            ft.Column([
                ft.ElevatedButton("新規作成", on_click=lambda _: dialog.open(True)),
                view_issued_button
            ])
        ]),
        ft.Divider(),
        issued_plans_textfield,
        dialog
    )

df_patients = load_patient_data()
ft.app(target=lambda page: main_async(page, df_patients))
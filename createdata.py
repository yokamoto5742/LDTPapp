import flet as ft
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import pandas as pd

# SQLAlchemyの設定
engine = create_engine('sqlite:///patient_info.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


# PatientInfoモデルの定義
class PatientInfo(Base):
    __tablename__ = 'patient_info'
    id = Column(Integer, primary_key=True)
    main_diagnosis = Column(String)
    creation_count = Column(String)
    target_weight = Column(String)
    goal1 = Column(String)
    goal2 = Column(String)
    diet = Column(String)
    exercise_prescription = Column(String)
    exercise_time = Column(String)
    exercise_frequency = Column(String)
    exercise_intensity = Column(String)
    daily_activity = Column(String)
    nonsmoker = Column(String)
    smoking_cessation = Column(String)
    other1 = Column(String)
    other2 = Column(String)


Base.metadata.create_all(engine)


def main(page: ft.Page):
    page.title = "Patient Information"
    page.scroll = "auto"

    def save_data(e):
        global selected_row
        session = Session()
        if selected_row is not None:
            patient_info = session.query(PatientInfo).filter(PatientInfo.id == selected_row['ID']).first()
            if patient_info:
                patient_info.main_diagnosis = main_diagnosis.value
                patient_info.creation_count = creation_count.value
                patient_info.target_weight = target_weight.value
                patient_info.goal1 = goal1.value
                patient_info.goal2 = goal2.value
                patient_info.diet = diet.value
                patient_info.exercise_prescription = exercise_prescription.value
                patient_info.exercise_time = exercise_time.value
                patient_info.exercise_frequency = exercise_frequency.value
                patient_info.exercise_intensity = exercise_intensity.value
                patient_info.daily_activity = daily_activity.value
                patient_info.nonsmoker = str(nonsmoker.value)
                patient_info.smoking_cessation = str(smoking_cessation.value)
                patient_info.other1 = other1.value
                patient_info.other2 = other2.value
                session.commit()
                page.snack_bar = ft.SnackBar(
                    ft.Text("データが更新されました"),
                    action="閉じる",
                )
                page.snack_bar.open = True
        else:
            selected_row = None
            patient_info = PatientInfo(
                main_diagnosis=main_diagnosis.value,
                creation_count=creation_count.value,
                target_weight=target_weight.value,
                goal1=goal1.value,
                goal2=goal2.value,
                diet=diet.value,
                exercise_prescription=exercise_prescription.value,
                exercise_time=exercise_time.value,
                exercise_frequency=exercise_frequency.value,
                exercise_intensity=exercise_intensity.value,
                daily_activity=daily_activity.value,
                nonsmoker=str(nonsmoker.value),
                smoking_cessation=str(smoking_cessation.value),
                other1=other1.value,
                other2=other2.value
            )
            session.add(patient_info)
            session.commit()
            page.snack_bar = ft.SnackBar(
                ft.Text("データが保存されました"),
                action="閉じる",
            )
            page.snack_bar.open = True

        session.close()
        update_history()
        page.update()

    def load_data(e):
        session = Session()
        patient_info = session.query(PatientInfo).order_by(PatientInfo.id.desc()).first()
        if patient_info:
            main_diagnosis.value = patient_info.main_diagnosis
            creation_count.value = patient_info.creation_count
            target_weight.value = patient_info.target_weight
            goal1.value = patient_info.goal1
            goal2.value = patient_info.goal2
            diet.value = patient_info.diet
            exercise_prescription.value = patient_info.exercise_prescription
            exercise_time.value = patient_info.exercise_time
            exercise_frequency.value = patient_info.exercise_frequency
            exercise_intensity.value = patient_info.exercise_intensity
            daily_activity.value = patient_info.daily_activity
            nonsmoker.value = patient_info.nonsmoker == 'True'
            smoking_cessation.value = patient_info.smoking_cessation == 'True'
            other1.value = patient_info.other1
            other2.value = patient_info.other2
        session.close()
        page.update()

    def delete_data(e):
        session = Session()
        patient_info = session.query(PatientInfo).order_by(PatientInfo.id.desc()).first()
        if patient_info:
            session.delete(patient_info)
            session.commit()
            page.snack_bar = ft.SnackBar(
                ft.Text("データが削除されました"),
                action="閉じる",
            )
            page.snack_bar.open = True
        session.close()
        update_history()
        page.update()

    def update_history():
        data = fetch_data()
        history.rows = create_data_rows(data)
        page.update()

    def on_row_selected(e):
        global selected_row
        if e.data == "true":
            row_index = history.rows.index(e.control)
            selected_row = history.rows[row_index].data

            session = Session()
            patient_info = session.query(PatientInfo).filter(PatientInfo.id == selected_row['ID']).first()
            if patient_info:
                main_diagnosis.value = patient_info.main_diagnosis
                creation_count.value = patient_info.creation_count
                target_weight.value = patient_info.target_weight
                goal1.value = patient_info.goal1
                goal2.value = patient_info.goal2
                diet.value = patient_info.diet
                exercise_prescription.value = patient_info.exercise_prescription
                exercise_time.value = patient_info.exercise_time
                exercise_frequency.value = patient_info.exercise_frequency
                exercise_intensity.value = patient_info.exercise_intensity
                daily_activity.value = patient_info.daily_activity
                nonsmoker.value = patient_info.nonsmoker == 'True'
                smoking_cessation.value = patient_info.smoking_cessation == 'True'
                other1.value = patient_info.other1
                other2.value = patient_info.other2
            session.close()
            page.update()

        if e.data == "true":
            row_index = history.rows.index(e.control)
            selected_row = history.rows[row_index].data

    def fetch_data():
        session = Session()
        patient_info_list = session.query(PatientInfo.id, PatientInfo.main_diagnosis, PatientInfo.creation_count).all()
        session.close()

        data = []
        for info in patient_info_list:
            data.append({
                "id": str(info.id),
                "disease": info.main_diagnosis,
                "count": info.creation_count
            })

        return data

    def create_data_rows(data):
        rows = []
        for item in data:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["id"])),
                    ft.DataCell(ft.Text(item["disease"])),
                    ft.DataCell(ft.Text(item["count"])),
                ],
                on_select_changed=on_row_selected,
                data={'ID': item["id"]}  # 行のデータに'ID'カラムを追加
            )
            rows.append(row)
        return rows

    # Patient Information
    main_diagnosis = ft.TextField(label="主病名", width=200, value="")
    creation_count = ft.TextField(label="作成回数", width=150, value="")
    target_weight = ft.TextField(label="目標体重", width=150, value="")

    # Goals
    goal1 = ft.TextField(label="①達成目標：患者と相談した目標", width=600, value="")
    goal2 = ft.TextField(label="②行動目標：患者と相談した目標", width=600, value="")

    # Guidance Items
    diet = ft.TextField(
        label="食事",
        multiline=True,
        disabled=False,
        value="食事量を適正にする\n食物繊維の摂取量を増やす\nゆっくり食べる\n間食を減らす",
        width=400,
    )
    exercise_prescription = ft.TextField(label="運動処方", width=400, value="ウォーキング")
    exercise_time = ft.TextField(label="時間", value="30分以上", width=200)
    exercise_frequency = ft.TextField(label="頻度", value="ほぼ毎日", width=200)
    exercise_intensity = ft.TextField(label="強度", value="少し汗をかく程度", width=200)
    daily_activity = ft.TextField(label="日常生活の活動量増加", value="1日8000歩以上", width=400)
    nonsmoker = ft.Checkbox(label="非喫煙者である")
    smoking_cessation = ft.Checkbox(label="禁煙の実施方法等を指示")
    other1 = ft.TextField(label="その他1", value="睡眠の確保１日７時間", width=300)
    other2 = ft.TextField(label="その他2", value="家庭での毎日の歩数の測定", width=300)

    guidance_items = ft.Column([
        diet,
        exercise_prescription,
        ft.Row([exercise_time, exercise_frequency, exercise_intensity]),
        daily_activity,
        ft.Text("たばこ", size=14),
        ft.Row([nonsmoker, smoking_cessation]),
        ft.Row([other1, other2]),
    ])

    selected_row = None
    data = fetch_data()
    rows = create_data_rows(data)


    history = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("主病名")),
            ft.DataColumn(ft.Text("作成回数")),
        ],
        rows=rows,
        width=1200,
        height=400,
    )

    buttons = ft.Row([
        ft.ElevatedButton("戻る", on_click=lambda _: page.go("/")),
        ft.ElevatedButton("保存", on_click=save_data),
        ft.ElevatedButton("読込", on_click=load_data),
        ft.ElevatedButton("削除", on_click=delete_data),
    ])

    # Layout
    layout = ft.Column([
        ft.Row([
            main_diagnosis,
            creation_count, ft.Text("回目", size=14), target_weight, ft.Text("kg", size=14)
        ]),
        goal1,
        goal2,
        guidance_items,
        buttons,
        history
    ])

    page.add(layout)
    update_history()


ft.app(target=main)

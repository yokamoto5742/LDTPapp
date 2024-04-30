import flet as ft

def main(page: ft.Page):
    page.title = "Patient Information"
    page.scroll = "auto"

    def button_click(e):
        pass

    # Patient Information
    patient_id = ft.TextField(label="患者ID", width=200, value="")
    name = ft.TextField(label="氏名", width=200, value="")
    kana = ft.TextField(label="カナ", width=200, value="")
    gender = ft.TextField(label="性別", width=200, value="")
    dob = ft.TextField(label="生年月日", width=200, value="")
    main_diagnosis = ft.TextField(label="主病名", width=200, value="")
    creation_count = ft.TextField(label="作成回数", width=150, value="")

    # Goals
    goal1 = ft.TextField(label="①達成目標：患者と相談した目標", width=600, value="")
    goal2 = ft.TextField(label="②行動目標：患者と相談した目標", width=600, value="")
    target_weight = ft.TextField(label="目標体重", width=150, value="")

    # Guidance Items
    guidance_items = ft.Column([
        ft.TextField(
            label="食事",
            multiline=True,
            disabled=False,
            value="食事量を適正にする\n食物繊維の摂取量を増やす\nゆっくり食べる\n間食を減らす",
            width=400,
        ),
        ft.TextField(label="運動処方", width=400, value="ウォーキング"),
        ft.Row([
            ft.TextField(label="時間",value="30分以上", width=200),
            ft.TextField(label="頻度",value="ほぼ毎日", width=200),
            ft.TextField(label="強度",value="少し汗をかく程度", width=200),
        ]),
        ft.TextField(label="日常生活の活動量増加", value="1日8000歩以上", width=400),
        ft.Text("たばこ", size=14),
        ft.Row([
            ft.Checkbox(label="非喫煙者である"),
            ft.Checkbox(label="禁煙の実施方法等を指示"),
        ]),
        ft.Row([
            ft.TextField(label="その他1", value="睡眠の確保１日７時間", width=300),
            ft.TextField(label="その他2", value="家庭での毎日の歩数の測定", width=300),
        ]),
    ])

    # Buttons
    buttons = ft.Row([
        ft.ElevatedButton("戻る", on_click=button_click),
        ft.ElevatedButton("保存", on_click=button_click),
    ])

    # Layout
    layout = ft.Column([
        ft.Row([
            main_diagnosis,
            creation_count, ft.Text("回目", size=14),target_weight, ft.Text("kg", size=14)
        ]),
        goal1,
        goal2,
        guidance_items,
        buttons
    ], scroll="auto")

    page.add(layout)

ft.app(target=main)

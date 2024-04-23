import flet as ft


class Home(ft.View):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        self.patient_id = ft.TextField(label="患者ID", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.name = ft.TextField(label="氏名", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.kana = ft.TextField(label="カナ", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.gender = ft.TextField(label="性別", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.birthday = ft.TextField(label="生年月日", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.doctor_id = ft.TextField(label="医師ID", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.doctor_name = ft.TextField(label="医師名", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.department = ft.TextField(label="診療科", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.disease_name = ft.TextField(label="主病名", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.plan_count = ft.TextField(label="作成回数", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)

        self.plan_list = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("発行日", size=ft.TextThemeStyle.BODY_SMALL)),
                ft.DataColumn(ft.Text("診療科", size=ft.TextThemeStyle.BODY_SMALL)),
                ft.DataColumn(ft.Text("医師名", size=ft.TextThemeStyle.BODY_SMALL)),
                ft.DataColumn(ft.Text("主病名", size=ft.TextThemeStyle.BODY_SMALL)),
                ft.DataColumn(ft.Text("作成回数", size=ft.TextThemeStyle.BODY_SMALL)),
            ],
            rows=[],
        )

        self.close_button = ft.ElevatedButton("閉じる", style=ft.ButtonStyle(padding=5))
        self.new_button = ft.ElevatedButton("新規作成", style=ft.ButtonStyle(padding=5), on_click=self.go_to_kenshin_monshin)
        self.print_save_button = ft.ElevatedButton("印刷保存", style=ft.ButtonStyle(padding=5))
        self.copy_last_button = ft.ElevatedButton("前回コピー", style=ft.ButtonStyle(padding=5))

        return ft.Column(
            controls=[
                ft.Row(controls=[self.patient_id, self.name, self.kana, self.gender, self.birthday]),
                ft.Row(controls=[self.doctor_id, self.doctor_name, self.department]),
                ft.Row(controls=[self.disease_name, self.plan_count]),
                self.plan_list,
                ft.Row(controls=[self.close_button, self.new_button, self.print_save_button, self.copy_last_button]),
            ],
        )

    def go_to_kenshin_monshin(self, e):
        self.page.go("/kenshin_monshin")


class KenshinMonshin(ft.View):
    def build(self):
        self.patient_id = ft.TextField(label="患者ID", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.name = ft.TextField(label="氏名", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.kana = ft.TextField(label="カナ", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.gender = ft.TextField(label="性別", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.birthday = ft.TextField(label="生年月日", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)

        self.height = ft.TextField(label="身長", suffix_text="cm", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.weight = ft.TextField(label="体重", suffix_text="kg", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.weight_goal = ft.TextField(label="目標体重", suffix_text="kg", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.bmi = ft.TextField(label="BMI", read_only=True, text_size=ft.TextThemeStyle.BODY_SMALL)
        self.abdominal_circumference = ft.TextField(label="腹囲", suffix_text="cm", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.abdominal_circumference_goal = ft.TextField(label="目標腹囲", suffix_text="cm", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.nutritional_status = ft.Dropdown(
            label="栄養状態",
            options=[
                ft.dropdown.Option("低栄養状態の恐れ"),
                ft.dropdown.Option("良好"),
                ft.dropdown.Option("肥満"),
            ],
            height=40,
            text_size=ft.TextThemeStyle.BODY_SMALL,
        )
        self.blood_pressure = ft.TextField(label="血圧", suffix_text="mmHg", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.blood_pressure_goal = ft.TextField(label="目標血圧", suffix_text="mmHg", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.exercise_ecg = ft.Checkbox(label="運動負荷心電図", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))
        self.other_exams = ft.TextField(label="その他検査", text_size=ft.TextThemeStyle.BODY_SMALL)

        self.diet = ft.Checkbox(label="食事の状況", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))
        self.exercise = ft.Checkbox(label="運動の状況", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))
        self.smoking = ft.Checkbox(label="喫煙", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))
        self.dental_checkup = ft.Checkbox(label="歯科の受診状況", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))
        self.other_lifestyle = ft.Checkbox(label="その他の生活", label_style=ft.TextStyle(size=ft.TextThemeStyle.BODY_SMALL))

        self.achievement_goal = ft.TextField(label="達成目標", hint_text="患者と相談した目標", text_size=ft.TextThemeStyle.BODY_SMALL)
        self.action_goal = ft.TextField(label="行動目標", hint_text="患者と相談した目標", text_size=ft.TextThemeStyle.BODY_SMALL)

        self.back_button = ft.ElevatedButton("戻る", style=ft.ButtonStyle(padding=5))
        self.next_button = ft.ElevatedButton("次へ", style=ft.ButtonStyle(padding=5))
        self.save_button = ft.ElevatedButton("保存", style=ft.ButtonStyle(padding=5))

        return ft.Column(
            controls=[
                ft.Row(controls=[self.patient_id, self.name, self.kana, self.gender, self.birthday]),
                ft.Text("検査項目", size=ft.TextThemeStyle.BODY_SMALL, weight=ft.FontWeight.BOLD),
                ft.Row(controls=[self.height, self.weight, self.weight_goal, self.bmi]),
                ft.Row(controls=[self.abdominal_circumference, self.abdominal_circumference_goal, self.nutritional_status]),
                ft.Row(controls=[self.blood_pressure, self.blood_pressure_goal]),
                ft.Row(controls=[self.exercise_ecg, self.other_exams]),
                ft.Text("問診", size=ft.TextThemeStyle.BODY_SMALL, weight=ft.FontWeight.BOLD),
                ft.Row(controls=[self.diet, self.exercise, self.smoking, self.dental_checkup, self.other_lifestyle]),
                self.achievement_goal,
                self.action_goal,
                ft.Row(controls=[self.back_button, self.next_button, self.save_button]),
            ],
        )


def main(page: ft.Page):
    page.title = "生活習慣病療養計画書"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    home = Home(page)
    kenshin_monshin = KenshinMonshin()

    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.views.append(home)
        elif page.route == "/kenshin_monshin":
            page.views.append(kenshin_monshin)
        page.update()

    page.on_route_change = route_change
    page.go("/home")


ft.app(target=main, view=ft.WEB_BROWSER)

import flet as ft


def main(page: ft.Page):
    page.title = "生活習慣病 療養計画書"
    page.scroll = "auto"

    def route_change(route):
        page.views.clear()
        if page.route == "/patient_info":
            page.views.append(view_patient_info())
        elif page.route == "/exam_info":
            page.views.append(view_exam_info())
        elif page.route == "/guidance_plan":
            page.views.append(view_guidance_plan())
        else:
            page.views.append(view_404())
        page.update()

    def view_patient_info():
        # 患者情報
        patient_info = ft.Row(controls=[
            ft.Column(controls=[
                ft.Text("患者氏名："),
                ft.Text("生年月日："),
            ]),
            ft.Column(controls=[
                ft.Text("（ 男 ・ 女 ）"),
                ft.Text("年 月 日生（ 才）"),
            ]),
        ])

        return ft.View(
            "/patient_info",
            [
                ft.AppBar(title=ft.Text("患者情報"), bgcolor=ft.colors.SURFACE_VARIANT),
                patient_info,
                ft.ElevatedButton("次へ", on_click=lambda _: page.go("/exam_info")),
            ]
        )

    def view_exam_info():
        # 検査・問診
        exam_info = ft.Column(controls=[
            ft.Text("【検査項目】"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("検査項目")),
                    ft.DataColumn(ft.Text("現在値")),
                    ft.DataColumn(ft.Text("目標値")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("身長")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("体重")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("BMI")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("腹囲")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("収縮期血圧")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("拡張期血圧")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("中性脂肪")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("HDLコレステロール")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("LDLコレステロール")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("HbA1c")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("その他")), ft.DataCell(ft.Text("")), ft.DataCell(ft.Text(""))]),
                ],
            ),
            ft.Text("【問診】"),
            ft.Row(controls=[
                ft.Checkbox(label="食事の状況"),
                ft.Checkbox(label="運動の状況"),
            ]),
            ft.Row(controls=[
                ft.Checkbox(label="喫煙"),
                ft.Checkbox(label="歯科受診"),
            ]),
        ])

        return ft.View(
            "/exam_info",
            [
                ft.AppBar(title=ft.Text("検査・問診"), bgcolor=ft.colors.SURFACE_VARIANT),
                exam_info,
                ft.Row(controls=[
                    ft.ElevatedButton("前へ", on_click=lambda _: page.go("/patient_info")),
                    ft.ElevatedButton("次へ", on_click=lambda _: page.go("/guidance_plan")),
                ]),
            ]
        )

    def view_guidance_plan():
        # 指導計画
        guidance_plan = ft.Column(controls=[
            ft.Text("【指導項目】患者と相談した目標"),
            ft.Row(controls=[
                ft.Checkbox(label="食事"),
                ft.Text("（ ）"),
            ]),
            ft.Row(controls=[
                ft.Checkbox(label="運動"),
                ft.Text("（ ）"),
            ]),
            ft.Row(controls=[
                ft.Checkbox(label="たばこ"),
                ft.Checkbox(label="その他（ ）"),
            ]),
            ft.Text("【指導の評価】"),
            ft.Row(controls=[
                ft.Radio("実施", value="done"),
                ft.Radio("継続の要否", value="continue"),
                ft.Radio("未達", value="unachieved"),
            ]),
        ])

        return ft.View(
            "/guidance_plan",
            [
                ft.AppBar(title=ft.Text("指導計画"), bgcolor=ft.colors.SURFACE_VARIANT),
                guidance_plan,
                ft.ElevatedButton("前へ", on_click=lambda _: page.go("/exam_info")),
            ]
        )

    def view_404():
        return ft.View(
            "/404",
            [
                ft.AppBar(title=ft.Text("ページが見つかりません"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("ページが見つかりませんでした。"),
            ]
        )

    page.on_route_change = route_change
    page.go("/patient_info")


ft.app(target=main, view=ft.WEB_BROWSER)

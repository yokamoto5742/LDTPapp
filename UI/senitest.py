import flet
from flet import AppBar, ElevatedButton, Page, Text, View


def main(page: Page):
    # ---------------------------------
    # 関数定義
    # ---------------------------------
    # ページを更新する
    def route_change(e):
        print("Route change:", e.route)

        # ページクリア
        page.views.clear()

        # トップページ（常にviewに追加する）
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("トップページ")),
                    ElevatedButton("テストページへ移動", on_click=open_test),
                ],
            )
        )
        # テストページ（テストページのときだけviewに追加する）
        if page.route == "/test":
            page.views.append(
                View(
                    "/test",
                    [
                        AppBar(title=Text("テストページ")),
                        Text("これはテストページです"),
                    ],
                )
            )

        # ページ更新
        page.update()

    # 現在のページを削除して、前のページに戻る
    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # テストページへ移動
    def open_test(e):
        page.go("/test")

    # ---------------------------------
    # イベントの登録
    # ---------------------------------
    # ページ遷移イベントが発生したら、ページを更新
    page.on_route_change = route_change
    # AppBarの戻るボタンクリック時、前のページへ戻る
    page.on_view_pop = view_pop

    # ---------------------------------
    # 起動時の処理
    # ---------------------------------
    # ページ遷移を実行
    page.go(page.route)


flet.app(target=main)
import sqlite3

import flet as ft
from flet import *


def main(page: Page):
    page.scrollTo = "always"

    mytable = DataTable(columns=[
        DataColumn(Text("id")),
        DataColumn(Text("namae")),
        DataColumn(Text("barthday")),
        DataColumn(Text("age")),
    ],
        rows=[],
    )
    page.add(mytable)

    def mydata(e):

        mytable.clear()
        page.update()

        dbname = "db/meibo.db"
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        sql = "SELECT * FROM t_meibo"
        cur.execute(sql)
        myrows = []
        for i in cur:
            row = DataRow(
                cells=[
                    DataCell(Text(i[0])),
                    DataCell(Text(i[1])),
                    DataCell(Text(i[2])),
                    DataCell(Text(i[3])),
                ],
            )
            myrows.append(row)
        conn.close()

        mytable = DataTable(columns=[
            DataColumn(Text("id")),
            DataColumn(Text("namae")),
            DataColumn(Text("barthday")),
            DataColumn(Text("age")),
        ],
            rows=myrows,
        )
        page.add(mytable)
        page.update()

    my_btn = ElevatedButton(
        "show data", bgcolor="red", color="white", on_click=mydata)
    page.add(my_btn)


ft.app(target=main)

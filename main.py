import os

import flet as ft
from sudachi import TokensReader, tokenize


def main(page: ft.Page):
    page.title = "SudachiPy"

    contents = ft.Ref[ft.Text]()
    copy_button = ft.Ref[ft.ElevatedButton]()
    is_ignore_paren = ft.Ref[ft.Switch]()
    result_table = ft.Ref[ft.DataTable]()

    ###################################
    # execute button
    ###################################

    def execute(_: ft.ControlEvent):
        if contents.current.value:
            copy_button.current.visible = False
            page.update()
            result_table.current.columns = [
                ft.DataColumn(ft.Text("Line")),
                ft.DataColumn(ft.Text("Reading")),
                ft.DataColumn(ft.Text("Detail")),
            ]
            table_rows = []
            for parsed_line in tokenize(contents.current.value.strip().splitlines(), is_ignore_paren.current.value):
                reader = TokensReader(parsed_line.tokens)
                table_rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(parsed_line.line)),
                    ft.DataCell(ft.Text(reader.get_reading())),
                    ft.DataCell(ft.Text(reader.get_detail())),
                ]))
            result_table.current.rows = table_rows
            copy_button.current.visible = True
            copy_button.current.text = "COPY!"
            page.update()

    def copy_table(_: ft.ControlEvent):
        lines = []
        for r in result_table.current.rows:
            lines.append("\t".join([c.content.value for c in r.cells]))
        page.set_clipboard(os.linesep.join(lines))
        copy_button.current.text = "COPIED!"
        page.update()

    ###################################
    # render page
    ###################################

    ui_cols = [
        ft.Text(
            "github.com/AWtnb/flet_sudachiPy",
            style="labelSmall",
            weight="bold",
            color=ft.colors.BLUE_400,
        ),
        ft.TextField(
            ref=contents,
            label="input here!",
            multiline=True,
            autofocus=True,
            value="",
        ),
        ft.Row(controls=[
            ft.FilledButton("GO!", on_click=execute),
            ft.Switch(ref=is_ignore_paren,
                      label="Skip inside: () / []", value=True),
        ]),
        ft.Divider(),
        ft.ElevatedButton(ref=copy_button, text="COPY!",
                          on_click=copy_table, visible=False),
        ft.DataTable(ref=result_table)
    ]

    page.add(ft.Column(controls=ui_cols))


ft.app(target=main)

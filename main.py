import os
from webbrowser import open

import flet as ft
from sudachi import TokensReader, tokenize


def main(page: ft.Page):
    page.title = "flet-yomi"

    contents = ft.Ref[ft.Text]()
    copy_button = ft.Ref[ft.ElevatedButton]()
    is_ignore_paren = ft.Ref[ft.Switch]()
    is_focus_name = ft.Ref[ft.Switch]()
    result_table = ft.Ref[ft.DataTable]()

    ###################################
    # execute button
    ###################################

    def execute(_: ft.ControlEvent):
        if contents.current.value:
            copy_button.current.visible = False
            page.update()
            table_rows = []
            parsed_lines = tokenize(
                contents.current.value.strip().splitlines(),
                is_ignore_paren.current.value,
                is_focus_name.current.value,
            )
            for parsed_line in parsed_lines:
                reader = TokensReader(parsed_line.tokens)
                table_rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(parsed_line.raw_line)),
                            ft.DataCell(ft.Text(reader.get_reading())),
                            ft.DataCell(ft.Text(reader.get_detail())),
                        ]
                    )
                )
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
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "YOMI", size=40, weight=ft.FontWeight.BOLD, italic=True
                    ),
                    alignment=ft.alignment.top_left,
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.SOURCE_OUTLINED,
                        icon_color=ft.colors.BLUE_400,
                        on_click=lambda _: open("https://github.com/AWtnb/flet-yomi"),
                    ),
                    alignment=ft.alignment.top_right,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.TextField(
            ref=contents,
            label="input here!",
            multiline=True,
            autofocus=True,
            value="",
            max_lines=6,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(
                    "GO!",
                    on_click=execute,
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE},
                        bgcolor={"": ft.colors.BLUE_ACCENT_700},
                        side={
                            ft.MaterialState.HOVERED: ft.border.BorderSide(
                                2, ft.colors.RED_ACCENT
                            ),
                            ft.MaterialState.FOCUSED: ft.border.BorderSide(
                                2, ft.colors.RED_ACCENT
                            ),
                        },
                    ),
                ),
            ]
        ),
        ft.Row(
            controls=[
                ft.Switch(
                    ref=is_ignore_paren, label="Skip inside: () / []", value=True
                ),
                ft.Switch(
                    ref=is_focus_name,
                    label="Skip nombles or reference (for book index)",
                    value=True,
                ),
            ]
        ),
        ft.Divider(),
        ft.FilledButton(
            ref=copy_button, text="COPY!", on_click=copy_table, visible=False
        ),
        ft.ListView(
            controls=[
                ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Line")),
                        ft.DataColumn(ft.Text("Reading")),
                        ft.DataColumn(ft.Text("Detail")),
                    ],
                    ref=result_table,
                )
            ],
            height=400,
        ),
    ]
    page.add(ft.Column(controls=ui_cols))


ft.app(target=main, assets_dir="assets")

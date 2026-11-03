import json
from pathlib import Path

import flet as ft

from json_converter import FileWay, JsonConverter


OUTPUT_PATH = Path(__file__).resolve().parents[1] / "output.json"


def main(page: ft.Page) -> None:
    page.title = "JSON-конвертер"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_field = ft.TextField(
        label="Введите обычный текст или JSON",
        hint_text='Например: {"name": "Анна"}',
        multiline=True,
        min_lines=3,
        max_lines=8,
        width=420,
    )
    status = ft.Text()

    def convert_input(_: ft.ControlEvent) -> None:
        raw_value = text_field.value or ""
        if not raw_value.strip():
            status.value = "Введите текст или JSON для конвертации."
            status.color = ft.Colors.RED
            page.update()
            return

        try:
            try:
                data = json.loads(raw_value)
            except json.JSONDecodeError:
                data = raw_value

            converter = JsonConverter(
                data=data,
                conversion=FileWay(OUTPUT_PATH),
            )
            output_path = converter.convert()
        except (OSError, TypeError, ValueError) as error:
            status.value = f"Не удалось сохранить JSON: {error}"
            status.color = ft.Colors.RED
        else:
            status.value = f"JSON сохранён в файл: {output_path}"
            status.color = ft.Colors.GREEN

        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text("Конвертер в JSON", size=28, weight=ft.FontWeight.BOLD),
                text_field,
                ft.FilledButton("Конвертировать", on_click=convert_input),
                status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
        )
    )

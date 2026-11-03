import flet as ft
from view.view_user import ViewUser
import jsone-converator.json-convertor

def main(page: ft.Page):
    # Налаштування вікна
    page.title = "Мій перший додаток"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Додавання елементів на сторінку
    page.add(
        ft.Text("Конверт то json", size=30, color="blue")
    )
    text_field = ft.TextField(label="Введіть файл або дані для конвертації в JSON", width=300)
    greeting = ft.Text()

    # Функція, яка спрацює при натисканні на кнопку
    def button_click(e):
        greeting.value = f"запуск!"
        page.update() # Оновлюємо сторінку, щоб побачити зміни
    def save_to_json():
        Convertor(data=[text_field.value]).getconvert_to_json = jsone-converator.json-convertor.FileWay(file_path=pathlib.Path("output.json"))
        Convertor(data=[text_field.value]).getconvert_to_json.convert_to_json()
        """
        идея с пакета josne-converator брать делать екзепляр класа и по с его методами добваляя сюа делать весь процес
        """

    submit_btn = ft.ElevatedButton("конверировать", on_click=button_click)




# Запуск додатка (target вказує на головну функцію)
ft.run(target=main, view=ft.WEB_BROWSER)


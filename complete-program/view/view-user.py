import flet as ft
from view.view_user import ViewUser

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
        greeting.value = f"Привіт, {text_field.value}!"
        page.update() # Оновлюємо сторінку, щоб побачити зміни

    submit_btn = ft.ElevatedButton("Привітатися", on_click=button_click)




# Запуск додатка (target вказує на головну функцію)
ft.run(target=main, view=ft.WEB_BROWSER)


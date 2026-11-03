import logging

import flet as ft

from view.view_user import main


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
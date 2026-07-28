import customtkinter as ctk

from app.config.settings import settings

from app.database.database import initialize_database
from app.ui.app_shell import AppShell
from app.core.language_manager import language_manager
from app.ui.create_account_page import CreateAccountPage
from app.ui.login_page import LoginPage
from app.ui.language_setup import LanguageSetup



def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    initialize_database()

    window = ctk.CTk()


    def language_selected(language):

        language_manager.set_interface_language(language)

        language_page.destroy()

        show_login()


    window.title(
        f"{settings.app_name} v{settings.version}"
    )

    window.geometry("1200x700")
    window.minsize(1000, 650)

    def clear_window():

        for widget in window.winfo_children():
            widget.destroy()


    def show_login():

        clear_window()

        LoginPage(
            window,
            on_login=login_success,
            on_create_account=show_create_account,
            on_change_language=show_language
        )

    def show_language():

        clear_window()

        LanguageSetup(
            window,
            language_selected
        )

    def show_create_account():

        clear_window()

        CreateAccountPage(
            window,
            language=language_manager.get_interface_language(),
            on_back=show_login
        )

    def login_success():

        for widget in window.winfo_children():
            widget.destroy()

        app_shell = AppShell(window)

        language_manager.listeners.clear()

        language_manager.add_listener(
            app_shell.refresh
        )

    language_page = LanguageSetup(
        window,
        language_selected
)

    window.mainloop()
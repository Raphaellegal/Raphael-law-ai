import customtkinter as ctk

from app.config.settings import settings
from app.core.language_manager import language_manager
from app.ui.translations import t
from app.ui.layout_manager import is_rtl


class SettingsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text=t("settings"),
            font=("Arial", 22, "bold")
        )

        title.pack(
            padx=20,
            pady=20
        )


        app_info = ctk.CTkLabel(
            self,
            text=(
                f"Application: {settings.app_name}\n"
                f"Version: {settings.version}\n"
                f"AI Provider: {settings.ai_provider}"
            ),
            justify="right" if is_rtl() else "left"
        )

        app_info.pack(
            anchor="e" if is_rtl() else "w",
            padx=20,
            pady=10
        )


        language_label = ctk.CTkLabel(
            self,
            text=t("interface_language")
        )

        language_label.pack(
            anchor="e" if is_rtl() else "w",
            padx=20,
            pady=(20,5)
        )


        self.language_menu = ctk.CTkOptionMenu(
            self,
            values=list(settings.available_languages.keys()),
            command=self.change_language
        )

        self.language_menu.set(
            settings.language
        )

        self.language_menu.pack(
            padx=20,
            anchor="e" if is_rtl() else "w"
        )


    def change_language(self, choice):

        language_manager.set_interface_language(
            settings.available_languages[choice]
        )

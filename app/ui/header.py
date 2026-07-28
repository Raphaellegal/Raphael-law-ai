import customtkinter as ctk

from app.ui.translations import t
from app.ui.layout_manager import is_rtl


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="x")

        title = ctk.CTkLabel(
            self,
            text="⚖ RAPHAEL LEGAL AI",
            font=("Arial", 24, "bold")
        )

        title.pack(
            side="right" if is_rtl() else "left",
            padx=20,
            pady=15
        )

        about_button = ctk.CTkButton(
            self,
            text=t("about"),
            width=90
        )

        about_button.pack(
            side="left" if is_rtl() else "right",
            padx=20
        )
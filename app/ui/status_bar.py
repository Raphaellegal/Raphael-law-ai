import customtkinter as ctk

from app.ui.translations import t
from app.ui.layout_manager import is_rtl


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=30)

        self.pack_propagate(False)

        label = ctk.CTkLabel(
            self,
            text=t("status_ready")
        )

        label.pack(
            side="right" if is_rtl() else "left",
            padx=10
        )
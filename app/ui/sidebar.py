import customtkinter as ctk

from app.ui.translations import t
from app.ui.layout_manager import is_rtl

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220)
        self.configure(width=220)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="⚖️ Raphael",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=(20, 25))

        self.chat_button = ctk.CTkButton(
            self,
            text="💬  " + t("chat"),
            anchor="e" if is_rtl() else "w",
            height=30
        )
        self.chat_button.pack(fill="x", padx=15, pady=3)

        self.documents_button = ctk.CTkButton(
            self,
            text="📚  " + t("legal_documents"),
            anchor="e" if is_rtl() else "w",
            height=30
        )
        self.documents_button.pack(fill="x", padx=15, pady=3)

        self.settings_button = ctk.CTkButton(
            self,
            text="⚙️  " + t("settings"),
            anchor="e" if is_rtl() else "w",
            height=30
        )
        self.settings_button.pack(fill="x", padx=15, pady=3)

        ctk.CTkFrame(self, height=2).pack(
            fill="x",
            padx=15,
            pady=20
        )

        import_button = ctk.CTkButton(
            self,
            text="📥  " + t("import_document"),

        )
        import_button.pack(
            side="bottom",
            padx=15,
            pady=20,
            fill="x"
        )
    def set_active(self, button_name):

        # Reset all buttons
        buttons = [
            self.chat_button,
            self.documents_button,
            self.settings_button
        ]

        for button in buttons:
            button.configure(
                fg_color="transparent",
                hover_color="#2B2B2B"
            )


        # Highlight selected button
        if button_name == "chat":

            self.chat_button.configure(
                fg_color="#1F6AA5",
                hover_color="#1F6AA5"
            )


        elif button_name == "documents":

            self.documents_button.configure(
                fg_color="#1F6AA5",
                hover_color="#1F6AA5"
            )


        elif button_name == "settings":

            self.settings_button.configure(
                fg_color="#1F6AA5",
                hover_color="#1F6AA5"
            )       
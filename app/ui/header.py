import customtkinter as ctk


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
            side="left",
            padx=20,
            pady=15
        )

        about_button = ctk.CTkButton(
            self,
            text="About",
            width=90
        )

        about_button.pack(
            side="right",
            padx=20
        )
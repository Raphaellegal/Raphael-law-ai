import customtkinter as ctk


class LanguageSetup(ctk.CTkFrame):

    def __init__(self, master, on_language_selected):

        super().__init__(master)

        self.on_language_selected = on_language_selected


        self.pack(
            fill="both",
            expand=True
        )


        title = ctk.CTkLabel(
            self,
            text="Choose your language",
            font=("Arial", 28)
        )

        title.pack(
            pady=50
        )


        languages = [
            ("🇹🇳 العربية", "ar"),
            ("🇫🇷 Français", "fr"),
            ("🇬🇧 English", "en")
        ]


        for name, code in languages:

            button = ctk.CTkButton(
                self,
                text=name,
                width=250,
                height=50,
                command=lambda c=code: self.select(c)
            )

            button.pack(
                pady=10
            )


    def select(self, language):

        self.on_language_selected(language)
import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=220)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="📚 Documents",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(20, 15))

        categories = [
            "Labour Law",
            "Contracts",
            "Civil Law",
            "Criminal Law"
        ]

        for category in categories:
            button = ctk.CTkButton(
                self,
                text=category
            )
            button.pack(fill="x", padx=15, pady=5)

        import_button = ctk.CTkButton(
            self,
            text="+ Import Document"
        )
        import_button.pack(side="bottom", padx=15, pady=20, fill="x")
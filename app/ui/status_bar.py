import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=30)

        self.pack_propagate(False)

        label = ctk.CTkLabel(
            self,
            text="Status: Ready"
        )

        label.pack(side="left", padx=10)
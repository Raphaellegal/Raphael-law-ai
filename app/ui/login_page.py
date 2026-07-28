import customtkinter as ctk

from app.ui.translations import t
from app.ui.create_account_page import CreateAccountPage
from app.auth.user_manager import user_manager
from app.auth.session import session
from tkinter import messagebox


class LoginPage(ctk.CTkFrame):

    def __init__(

        self,
        master,
        on_login,
        on_create_account,
        on_change_language
    ):


        super().__init__(master)

        self.on_login = on_login

        self.on_create_account = on_create_account

        self.on_change_language = on_change_language

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Raphael Legal AI",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(50, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Welcome",
            font=("Arial", 18)
        )
        subtitle.pack(pady=(0, 30))

        self.email = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text=t(
                "email"
            )
        )
        self.email.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text=t(
                "password"
            ),
            show="*"
        )
        self.password.pack(pady=10)

        login_button = ctk.CTkButton(
            self,
            text=t(
                "login"
            ),
            command=self.login
        )
        login_button.pack(pady=20)

        create_button = ctk.CTkButton(
            self,
            text=t(
                "create_account"
            ),
            command=self.create_account
        )
        create_button.pack()

        language_button = ctk.CTkButton(
            self,
            text=t(
                "change_language"
            ),
            command=self.change_language
        )

        language_button.pack(
            pady=20
        )

    def login(self):

        email = self.email.get()

        password = self.password.get()

        if not self.email.get().strip():

            messagebox.showerror(
                "Missing Information",
                "Please enter your email."
            )

            return


        if not self.password.get():

            messagebox.showerror(
                "Missing Information",
                "Please enter your password."
            )

            return

        user = user_manager.authenticate(
            email,
            password
        )


        if user:

            session.login(user)

            self.on_login()


        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid email or password"
            )
    
    def create_account(self):

        for widget in self.master.winfo_children():
            widget.destroy()

        self.on_create_account()

    def change_language(self):

        self.on_change_language()
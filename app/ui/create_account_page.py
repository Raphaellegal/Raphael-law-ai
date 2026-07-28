import customtkinter as ctk

from app.auth.user_manager import user_manager
from app.auth.password import hash_password
from app.database.models import User
from app.ui.translations import t
from app.config.account_types import ACCOUNT_TYPES
from app.ui.messages import show_error

class CreateAccountPage(ctk.CTkFrame):

    def __init__(self, master, on_back, language):

        super().__init__(master)


        self.on_back = on_back

        self.pack(
            fill="both",
            expand=True
        )


        title = ctk.CTkLabel(
            self,
            text=t("create_account"),
            font=("Arial", 30, "bold")
        )

        title.pack(
            pady=(40, 10)
        )


        self.name = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text=t("full_name")
        )

        self.name.pack(pady=10)


        self.email = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text=t("email")
        )

        self.email.pack(pady=10)


        self.password = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text=t("password"),
            show="*"
        )

        self.password.pack(pady=10)


        self.confirm_password = ctk.CTkEntry(
            self,
            width=350,
            placeholder_text=t("confirm_password"),
            show="*"
        )

        self.confirm_password.pack(pady=10)

        self.account_type = ctk.CTkOptionMenu(
            self,
            values=list(ACCOUNT_TYPES.keys()),
            command=self.update_roles
        )

        self.account_type.set(
            "Select account type"
        )

        self.account_type.pack(
            pady=10
        )     

        self.role = ctk.CTkOptionMenu(
            self,
            values=[
                "Select role"
            ]
        )

        self.role.set(
            "Select role"
        )

        self.role.pack(
            pady=10
        )   


        create_button = ctk.CTkButton(
            self,
            text=t("create_account"),
            command=self.create_account
        )

        create_button.pack(
            pady=(30, 10)
        )


        back_button = ctk.CTkButton(
            self,
            text=t("back"),
            command=self.on_back
        )

        back_button.pack()

    def create_account(self):


        if not self.name.get().strip():

            show_error(
                "Missing Information",
                "Please enter your full name."
            )

            return


        if not self.email.get().strip():

            show_error(
                "Missing Information",
                "Please enter your email."
            )

            return


        if not self.password.get():

            show_error(
                "Missing Information",
                "Please enter a password."
            )

            return


        if not self.confirm_password.get():

            show_error(
                "Missing Information",
                "Please confirm your password."
            )

            return

        existing_user = user_manager.get_user_by_email(
            self.email.get()
        )

        if existing_user:

            show_error(
                "Account Exists",
                "An account with this email already exists."
            )

            return

        if self.password.get() != self.confirm_password.get():

            show_error(
                "Password Error",
                "Passwords do not match."
            )

            return

        if self.account_type.get() == "Select account type":

            show_error(
                "Missing Information",
                "Please select an account type"
            )

            return


        if self.role.get() == "Select role":

            show_error(
                "Missing Information",
                "Please select a role"
            )

            return

        user = User(

            id=None,

            full_name=self.name.get(),

            email=self.email.get(),

            password_hash=hash_password(
                self.password.get()
            ),

            category=ACCOUNT_TYPES[
                self.account_type.get()
            ]["category"],

            role=self.role.get(),

        )

        user_manager.create_user(user)

        self.on_back()

    def update_roles(self, choice):

        roles = ACCOUNT_TYPES[choice]["roles"]

        self.role.configure(
            values=roles
        )

        self.role.set(
            roles[0]
        )

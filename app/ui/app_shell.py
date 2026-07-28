import customtkinter as ctk

from app.core.language_manager import language_manager
from app.ui.layout_manager import is_rtl
from app.ui.header import Header
from app.ui.sidebar import Sidebar
from app.ui.chat_area import ChatArea
from app.ui.status_bar import StatusBar
from app.ui.settings_page import SettingsPage


class AppShell:

    def __init__(self, window):

        self.window = window

        self.language = language_manager.get_interface_language()

        self.build()

    def build(self):

        Header(self.window)

        main_frame = ctk.CTkFrame(self.window)

        main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )


        if is_rtl():

            main_frame.grid_columnconfigure(
                0,
                weight=1
            )

            main_frame.grid_columnconfigure(
                1,
                weight=0,
                minsize=220
            )

        else:

            main_frame.grid_columnconfigure(
                0,
                weight=0,
                minsize=220
            )

            main_frame.grid_columnconfigure(
                1,
                weight=1
            )


        main_frame.grid_rowconfigure(
            0,
            weight=1
        )   

        # Sidebar

        self.sidebar = Sidebar(main_frame)


        if is_rtl():

            self.sidebar.grid(
                row=0,
                column=1,
                sticky="nsew",
                padx=(10,0)
            )

        else:

            self.sidebar.grid(
                row=0,
                column=0,
                sticky="nsew",
                padx=(0,10)
            )


        # Page container

        self.page_container = ctk.CTkFrame(
            main_frame
        )


        if is_rtl():

            self.page_container.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        else:

            self.page_container.grid(
                row=0,
                column=1,
                sticky="nsew"
            )


        self.page_container.grid_rowconfigure(
            0,
            weight=1
        )

        self.page_container.grid_columnconfigure(
            0,
            weight=1
        )

        self.connect_buttons()

        self.show_chat()

        self.status_bar = StatusBar(
            self.window
        )

        self.status_bar.pack(
            fill="x"
        )

    def clear_page(self):

        for widget in self.page_container.winfo_children():
            widget.destroy()

    def show_chat(self):

        self.clear_page()

        self.sidebar.set_active("chat")

        ChatArea(
            self.page_container
        ).grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    def show_settings(self):

        self.clear_page()

        self.sidebar.set_active("settings")

        SettingsPage(
            self.page_container
        ).grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    def connect_buttons(self):

        self.sidebar.chat_button.configure(
            command=self.show_chat
        )


        self.sidebar.settings_button.configure(
            command=self.show_settings
        )

    def refresh(self):

        self.language = language_manager.get_interface_language()

        for widget in self.window.winfo_children():
            widget.destroy()

        self.build()


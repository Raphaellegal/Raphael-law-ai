import customtkinter as ctk

from app.ui.header import Header
from app.ui.sidebar import Sidebar
from app.ui.chat_area import ChatArea
from app.ui.status_bar import StatusBar


def start_gui():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()

    window.title("Raphael Legal AI")

    window.geometry("1200x700")
    window.minsize(1000, 650)

    # ================= HEADER =================

    Header(window)

    # ================= MAIN AREA =================

    main_frame = ctk.CTkFrame(window)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # configure grid layout (THIS IS IMPORTANT)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=4)
    main_frame.grid_rowconfigure(0, weight=1)

    # Sidebar (left)
    sidebar = Sidebar(main_frame)
    sidebar.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

    # Chat area (right)
    chat = ChatArea(main_frame)
    chat.grid(row=0, column=1, sticky="nsew")

    # ================= STATUS BAR =================

    StatusBar(window).pack(fill="x")

    window.mainloop()
import customtkinter as ctk
from app.core.raphael_brain import RaphaelBrain
from app.ui.translations import t
from app.ui.layout_manager import is_rtl
import time


class ChatArea(ctk.CTkFrame):

    def __init__(self, master):

        self.brain = RaphaelBrain()
        super().__init__(master)

        # ================= TITLE =================
        title = ctk.CTkLabel(
            self,
            text="💬 " + t("chat_with_raphael"),
            font=("Arial", 20, "bold")
        )

        title.pack(
            anchor="e" if is_rtl() else "w",
            padx=20,
            pady=(15, 10)
        )

        # ================= CHAT AREA (scrollable) =================
        self.chat_scroll = ctk.CTkScrollableFrame(self)
        self.chat_scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 10)
        )

        # ================= INPUT AREA =================
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="x", padx=20, pady=(0, 15))

        self.question = ctk.CTkTextbox(
            input_frame,
            height=60,
            wrap="word"
        )

        self.question.configure(
            wrap="word"
        )

        self.question.pack(
            side="right" if is_rtl() else "left",
            fill="x",
            expand=True,
            padx=(10,0) if is_rtl() else (0,10)
        )

        self.ask_button = ctk.CTkButton(
            input_frame,
            text=t("ask"),
            width=100,
            command=self.ask
        )
        self.ask_button.pack(
            side="left" if is_rtl() else "right"
        )

        self.question.bind("<Return>", self.on_enter)

    # ================= UI HELPERS =================

    def add_user_message(self, text):

        row = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        row.pack(fill="x", pady=6)

        bubble = ctk.CTkFrame(
            row,
            fg_color="#2B6EF3",
            corner_radius=12
        )

        bubble.pack(anchor="e", padx=10)

        label = ctk.CTkLabel(
            bubble,
            text=text,
            wraplength=420,
            justify="left",
            text_color="white"
        )

        label.pack(padx=12, pady=8)


    def add_bot_message(self, text):

        row = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        row.pack(fill="x", padx=20, pady=(8, 12))

        # Raphael title
        title = ctk.CTkLabel(
            row,
            text="⚖️ Raphael",
            font=("Arial", 14, "bold"),
            text_color="#808080",
            anchor="w"
        )
        title.pack(
            anchor="e" if is_rtl() else "w",
            pady=(0,5)
        )

        # Response text (no bubble)
        answer = ctk.CTkLabel(
            row,
            text=text,
            justify="right" if is_rtl() else "left",
            anchor="e" if is_rtl() else "w",
            wraplength=700
        )
        answer.pack(
            anchor="e" if is_rtl() else "w"
        )

    def scroll_to_bottom(self):
        self.chat_scroll.update_idletasks()
        self.chat_scroll._parent_canvas.yview_moveto(1.0)
        

    # ================= LOGIC =================

    def ask(self):

        question = self.question.get("1.0", "end").strip()

        if not question:
            return

        self.add_user_message(question)

        self.question.delete("1.0", "end")

        # 🔥 force UI update before AI work
        self.chat_scroll.update_idletasks()

        response = self.brain.think(question)

        if not response:
            response = "I don't have enough information in the legal documents yet."


        self.add_bot_message(response)

        # 🔥 safe scroll AFTER everything
        self.scroll_to_bottom()


    def focus_last_interaction(self):
        self.chat_scroll.update_idletasks()

        # scroll to bottom so latest pair is fully visible
        self.chat_scroll._parent_canvas.yview_moveto(1.0)

    def scroll_to_bottom(self):
        self.chat_scroll.after(50, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))


    def on_enter(self, event):
        self.ask()
        return "break"
    
    
from typing import Callable


class LanguageManager:
    """
    Handles interface and conversation languages.
    """

    def __init__(self):

        self.interface_language = "en"

        self.conversation_language = "auto"


        self.listeners = []

    def set_interface_language(self, language: str):

        self.interface_language = language

        self.notify_language_change()


    def get_interface_language(self):

        return self.interface_language


    def set_conversation_language(self, language: str):

        self.conversation_language = language


    def set_detected_conversation_language(self, language: str):

        self.conversation_language = language
        

    def get_conversation_language(self):

        return self.conversation_language

    def add_listener(self, callback: Callable):

        self.listeners.append(callback)


    def notify_language_change(self):

        for callback in self.listeners:
            callback()
    
language_manager = LanguageManager()


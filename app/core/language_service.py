from app.services.language_detector import LanguageDetector
from app.core.language_manager import LanguageManager


class LanguageService:

    def __init__(self):

        self.detector = LanguageDetector()
        self.language_manager = LanguageManager()


    def process_message(self, text: str):

        language = self.detector.detect_language(text)

        self.language_manager.set_detected_conversation_language(
            language
        )

        return language
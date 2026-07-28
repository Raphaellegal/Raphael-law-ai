from langdetect import detect


class LanguageDetector:
    """
    Detects the language of user messages.
    """

    def detect_language(self, text: str):

        try:
            return detect(text)

        except Exception:
            return "en"
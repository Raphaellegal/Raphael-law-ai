from app.services.language_detector import LanguageDetector


detector = LanguageDetector()


tests = [
    "What are workers rights?",
    "Quels sont les droits des travailleurs ?",
    "ما هي حقوق العمال ؟"
]


for text in tests:

    print(
        text,
        "=>",
        detector.detect_language(text)
    )
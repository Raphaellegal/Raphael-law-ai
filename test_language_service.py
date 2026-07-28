from app.core.language_service import LanguageService


service = LanguageService()


tests = [
    "What are workers rights?",
    "Quels sont les droits des travailleurs ?",
    "ما هي حقوق العمال ؟"
]


for text in tests:

    language = service.process_message(text)

    print(
        text,
        "=>",
        language
    )
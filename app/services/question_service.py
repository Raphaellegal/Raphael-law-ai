from app.brain import ask_question


class QuestionService:
    @staticmethod
    def answer(question: str) -> str:
        return ask_question(question)
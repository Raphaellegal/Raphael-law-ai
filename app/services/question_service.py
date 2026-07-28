from app.core.raphael_brain import RaphaelBrain


class QuestionService:

    brain = RaphaelBrain()

    @staticmethod
    def answer(question: str) -> str:
        return QuestionService.brain.think(question)
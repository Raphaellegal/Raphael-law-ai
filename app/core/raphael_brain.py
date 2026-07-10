from app.core.legal_response_engine import LegalResponseEngine


class RaphaelBrain:
    """
    Central decision-maker of Raphael.
    """

    def __init__(self):
        self.legal_engine = LegalResponseEngine()

    def think(self, question: str):
        """
        Process a user's question.
        """

        context = self.legal_engine.build_context(question)

        if not context.strip():
            return (
                "I could not find any relevant legal information "
                "in my current legal database."
            )

        return context
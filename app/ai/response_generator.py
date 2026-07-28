class ResponseGenerator:
    """
    Handles the final answer returned by the AI.
    """

    def generate(self, ai_response: str) -> str:

        if not ai_response.strip():
            return (
                "I could not generate a legal answer."
            )

        return ai_response.strip()
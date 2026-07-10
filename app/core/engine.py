from app.services.question_service import QuestionService


def process_question(question: str) -> str:
    """
    Main entry point for processing user questions.

    For now, it forwards the question to the current brain.
    Later, this function will decide whether to:
    - search legal documents,
    - use AI,
    - combine both,
    - manage conversation context.
    """

    return QuestionService.answer(question)
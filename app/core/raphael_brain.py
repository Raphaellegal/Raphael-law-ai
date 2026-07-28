from app.core.legal_response_engine import LegalResponseEngine
from app.ai.prompt_builder import PromptBuilder
from app.ai.ai_client import AIClient
from app.ai.response_generator import ResponseGenerator
from app.core.language_service import LanguageService


class RaphaelBrain:
    """
    Central decision-maker of Raphael.
    """

    def __init__(self):

        self.legal_engine = LegalResponseEngine()

        self.prompt_builder = PromptBuilder()

        self.ai_client = AIClient()

        self.response_generator = ResponseGenerator()

        self.language_service = LanguageService()


    def think(self, question: str):

        language = self.language_service.process_message(question)
        
        print("USER LANGUAGE:", language)

        # Step 1: Find legal information
        context = self.legal_engine.build_context(question)

        if not context.strip():
            return (
                "I could not find any relevant legal information "
                "in my current legal database."
            )


        # Step 2: Prepare AI prompt
        prompt = self.prompt_builder.build(
            question,
            context,
            language
        )


        # Step 3: Ask AI
        ai_response = self.ai_client.ask(prompt)


        # Step 4: Format final answer
        return self.response_generator.generate(
            ai_response
        )
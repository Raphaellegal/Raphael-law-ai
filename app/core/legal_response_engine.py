from app.core.knowledge import get_knowledge_service
from app.services.retriever import Retriever
from app.services.context_builder import ContextBuilder


class LegalResponseEngine:

    def __init__(self):
        self.retriever = Retriever()
        self.context_builder = ContextBuilder()

    def build_context(self, question: str):

        knowledge = get_knowledge_service()

        chunks = self.retriever.search(
            knowledge.knowledge_base.get_all_chunks(),
            question
        )

        return self.context_builder.build(chunks)
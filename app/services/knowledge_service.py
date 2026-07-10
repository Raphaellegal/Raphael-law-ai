from app.services.document_manager import DocumentManager
from app.services.knowledge_base import KnowledgeBase


class KnowledgeService:
    """
    Connects document loading with the knowledge base.
    """

    def __init__(self):
        self.document_manager = DocumentManager()
        self.knowledge_base = KnowledgeBase()

    def load_legal_documents(self, folder_path):
        """
        Load documents and store their chunks.
        """

        chunks = self.document_manager.load_documents(
            folder_path
        )

        self.knowledge_base.add_chunks(chunks)

    def get_knowledge_base(self):
        return self.knowledge_base
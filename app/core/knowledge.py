from app.services.knowledge_service import KnowledgeService
from app.config.settings import settings


knowledge_service = KnowledgeService()


def initialize_knowledge():
    """
    Load legal documents into memory.
    """

    knowledge_service.load_legal_documents(
        settings.documents_path
    )


def get_knowledge_service():
    return knowledge_service
from app.services.knowledge_service import KnowledgeService


knowledge_service = KnowledgeService()


def initialize_knowledge():
    """
    Load legal documents into memory.
    """

    knowledge_service.load_legal_documents(
        "legal_documents"
    )


def get_knowledge_service():
    return knowledge_service
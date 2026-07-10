from app.services.knowledge_service import KnowledgeService


service = KnowledgeService()

service.load_legal_documents(
    "legal_documents"
)

knowledge = service.get_knowledge_base()


print("Total chunks:")
print(knowledge.count())
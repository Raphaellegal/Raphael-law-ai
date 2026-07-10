from app.core.knowledge import (
    initialize_knowledge,
    get_knowledge_service
)


initialize_knowledge()


service = get_knowledge_service()

print(
    "Loaded chunks:",
    service.knowledge_base.count()
)
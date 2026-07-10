from app.core.knowledge import (
    initialize_knowledge,
    get_knowledge_service
)

from app.services.retriever import Retriever
from app.services.context_builder import ContextBuilder


initialize_knowledge()

knowledge = get_knowledge_service()

retriever = Retriever()
builder = ContextBuilder()


chunks = retriever.search(
    knowledge.knowledge_base.get_all_chunks(),
    "contract termination"
)


context = builder.build(chunks)


print(context)
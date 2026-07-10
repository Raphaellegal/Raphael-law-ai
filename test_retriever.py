from app.core.knowledge import (
    initialize_knowledge,
    get_knowledge_service
)

from app.services.retriever import Retriever


initialize_knowledge()

knowledge = get_knowledge_service()

retriever = Retriever()


results = retriever.search(
    knowledge.knowledge_base.get_all_chunks(),
    "contract termination"
)


print("Results:", len(results))

for result in results:
    print("----------------")
    print(result.content[:300])
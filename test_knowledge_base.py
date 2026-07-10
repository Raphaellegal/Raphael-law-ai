from app.services.document_loader import DocumentLoader
from app.services.document_processor import DocumentProcessor
from app.services.knowledge_base import KnowledgeBase


loader = DocumentLoader()
processor = DocumentProcessor()
knowledge = KnowledgeBase()


text = loader.load_text("labor_code/labor_code.txt")

chunks = processor.split_into_chunks(
    text,
    document_name="labor_code"
)

knowledge.add_chunks(chunks)


print("Total chunks:", knowledge.count())

print()
print("First chunk:")
print(knowledge.get_all_chunks()[0].content)
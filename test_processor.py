from app.services.document_loader import DocumentLoader
from app.services.document_processor import DocumentProcessor

loader = DocumentLoader()
processor = DocumentProcessor()

text = loader.load_text("labor_code/labor_code.txt")

chunks = processor.split_into_chunks(
    text,
    document_name="labor_code"
)

print(f"Number of chunks: {len(chunks)}")
print()
print("First chunk:")
print(chunks[0].document_name)
print(chunks[0].chunk_number)
print(chunks[0].content)
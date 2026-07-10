from app.services.document_manager import DocumentManager


manager = DocumentManager()

chunks = manager.load_documents(
    "legal_documents"
)

print("Total chunks:", len(chunks))

print()
print("First document:")
print(chunks[0].document_name)

print()
print(chunks[0].content)
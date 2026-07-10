from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

text = loader.load_text("labor_code/labor_code.txt")

print(text)
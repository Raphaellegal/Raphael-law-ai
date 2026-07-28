from app.services.pdf_reader import PDFReader


reader = PDFReader()

text = reader.read(
    "legal_documents/test_law.pdf"
)

print(text[:2000])
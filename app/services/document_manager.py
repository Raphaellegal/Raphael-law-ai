import os

from app.services.document_loader import DocumentLoader
from app.services.document_processor import DocumentProcessor


class DocumentManager:
    """
    Handles loading and processing legal document folders.
    """

    def __init__(self):
        self.loader = DocumentLoader()
        self.processor = DocumentProcessor()

    def load_documents(self, folder_path: str):

        all_chunks = []

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                if file.endswith(".txt"):

                    file_path = os.path.join(root, file)

                    print("MANAGER PATH:", file_path)

                    relative_path = os.path.relpath(
                        file_path,
                        "legal_documents"
                    )

                    text = self.loader.load_text(relative_path)

                    document_name = os.path.basename(root)

                    chunks = self.processor.split_into_chunks(
                        text,
                        document_name=document_name
                    )

                    all_chunks.extend(chunks)

        return all_chunks
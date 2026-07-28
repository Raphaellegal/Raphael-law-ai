import os

from app.services.document_pipeline import DocumentPipeline


class DocumentManager:
    """
    Handles loading and processing legal document folders.
    """

    def __init__(self):
        self.pipeline = DocumentPipeline()

    def load_documents(self, folder_path: str):

        all_chunks = []

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                print("FOUND FILE:", file)

                if file.endswith(".txt") or file.endswith(".pdf"):

                    file_path = os.path.join(root, file)

                    print("MANAGER PATH:", file_path)

                    relative_path = os.path.relpath(
                        file_path,
                        "legal_documents"
                    )

                    document_name = os.path.basename(root)

                    chunks = self.pipeline.process(
                        relative_path,
                        document_name
                    )

                    all_chunks.extend(chunks)

        return all_chunks
from app.services.document_manager import DocumentManager
from app.services.knowledge_base import KnowledgeBase
from app.services.embedding_service import EmbeddingService
from app.services.embedding_storage import EmbeddingStorage


class KnowledgeService:
    """
    Connects document loading with the knowledge base.
    """

    def __init__(self):

        self.document_manager = DocumentManager()
        self.knowledge_base = KnowledgeBase()
        self.embedding_service = EmbeddingService()
        self.storage = EmbeddingStorage()


    def load_legal_documents(self, folder_path):

        saved_chunks = self.storage.load()

        if saved_chunks:

            print("LOADING SAVED EMBEDDINGS")

            self.knowledge_base.add_chunks(
                saved_chunks
            )

            return


        print("CREATING NEW EMBEDDINGS")

        chunks = self.document_manager.load_documents(
            folder_path
        )


        for chunk in chunks:

            chunk.embedding = (
                self.embedding_service
                .create_embedding(
                    chunk.content
                )
            )


        self.storage.save(
            chunks
        )


        self.knowledge_base.add_chunks(
            chunks
        )


    def get_knowledge_base(self):
        return self.knowledge_base
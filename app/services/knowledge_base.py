from app.models.document_chunk import DocumentChunk


class KnowledgeBase:
    """
    Stores processed legal document chunks.
    """

    def __init__(self):
        self.chunks: list[DocumentChunk] = []

    def add_chunks(self, chunks: list[DocumentChunk]):
        """
        Add document chunks to the knowledge base.
        """

        self.chunks.extend(chunks)

    def get_all_chunks(self) -> list[DocumentChunk]:
        """
        Return all stored chunks.
        """

        return self.chunks

    def count(self) -> int:
        """
        Return number of stored chunks.
        """

        return len(self.chunks)
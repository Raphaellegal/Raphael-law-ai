from app.models.document_chunk import DocumentChunk
from app.services.embedding_service import EmbeddingService
import numpy as np


class Retriever:
    """
    Finds relevant legal information using semantic similarity.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()

    def search(
        self,
        chunks: list[DocumentChunk],
        query: str,
        limit: int = 3,
        threshold: float = 0.45
    ):

        query_embedding = self.embedding_service.create_embedding(
            query
        )

        results = []

        for chunk in chunks:

            if chunk.embedding is None:
                continue

            similarity = self.cosine_similarity(
                query_embedding,
                chunk.embedding
            )


            if similarity >= threshold:
                results.append(
                    (similarity, chunk)
                )

        results.sort(
            key=lambda x: x[0],
            reverse=True
        )

        selected = [
            chunk
            for score, chunk in results[:limit]
        ]

        return selected


    def cosine_similarity(self, a, b):

        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (
            np.linalg.norm(a)
            *
            np.linalg.norm(b)
        )
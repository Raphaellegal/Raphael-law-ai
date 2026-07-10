from app.models.document_chunk import DocumentChunk


class Retriever:
    """
    Finds relevant legal information.
    """

    def search(
        self,
        chunks: list[DocumentChunk],
        query: str,
        limit: int = 5
    ):
        """
        Temporary keyword search.
        Later replaced by semantic search.
        """

        results = []

        query_words = query.lower().split()

        for chunk in chunks:

            content = chunk.content.lower()

            score = sum(
                1
                for word in query_words
                if word in content
            )

            if score > 0:
                results.append(
                    (score, chunk)
                )

        results.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [
            chunk
            for score, chunk in results[:limit]
        ]
from app.models.document_chunk import DocumentChunk


class DocumentProcessor:
    """
    Splits legal documents into manageable chunks.
    """

    def split_into_chunks(
        self,
        text: str,
        document_name: str,
        max_lines: int = 10
    ) -> list[DocumentChunk]:
        """
        Split a legal document into chunks.
        """

        lines = text.splitlines()

        chunks = []
        current_chunk = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            current_chunk.append(line)

            if len(current_chunk) >= max_lines:
                chunks.append(
                    DocumentChunk(
                        document_name=document_name,
                        chunk_number=len(chunks) + 1,
                        content="\n".join(current_chunk)
                    )
                )

                current_chunk = []

        # Add the last chunk if there is one
        if current_chunk:
            chunks.append(
                DocumentChunk(
                    document_name=document_name,
                    chunk_number=len(chunks) + 1,
                    content="\n".join(current_chunk)
                )
            )

        return chunks
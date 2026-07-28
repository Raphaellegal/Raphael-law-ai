import re

from app.models.document_chunk import DocumentChunk


class DocumentProcessor:
    """
    Splits legal documents into meaningful sections.
    """

    def __init__(self):
        self.parser = LegalParser()

    def split_into_chunks(
        self,
        text: str,
        document_name: str
    ) -> list[DocumentChunk]:

        lines = text.splitlines()

        chunks = []

        current_chunk = []

        current_chapter = None
        current_article = None

        for line in lines:

            line = line.strip()

            if re.match(
                r"^(SECTION|CHAPTER|CHAPITRE|TITLE|TITRE)",
                line,
                re.IGNORECASE
            ):
                current_chapter = line

            if re.match(
                r"^ARTICLE",
                line,
                re.IGNORECASE
            ):
                current_article = line

            if not line:
                continue

            # New legal section detected
            if line.upper().startswith("SECTION") and current_chunk:

                chunks.append(
                    DocumentChunk(
                        document_name=document_name,
                        law_name=document_name,
                        chapter=current_chapter,
                        article=current_article,
                        chunk_number=len(chunks) + 1,
                        content="\n".join(current_chunk)
                    )
                )

                current_chunk = []

            current_chunk.append(line)

        # Add remaining section
        if current_chunk:

            chunks.append(
                DocumentChunk(
                    document_name=document_name,
                    law_name=document_name,
                    chapter=current_chapter,
                    article=current_article,
                    chunk_number=len(chunks) + 1,
                    content="\n".join(current_chunk)
                )
            )

        return chunks
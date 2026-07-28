from app.models.document_chunk import DocumentChunk
from app.models.legal_structure import LegalLaw


class ChunkBuilder:
    """
    Converts a parsed legal law into semantic chunks.
    """

    def build(self, law: LegalLaw):

        chunks = []

        chunk_number = 1

        for chapter in law.chapters:

            for article in chapter.articles:

                chunks.append(

                    DocumentChunk(

                        document_name=law.name,

                        law_name=law.name,

                        chapter=chapter.title,

                        article=article.number,

                        chunk_number=chunk_number,

                        content=article.content

                    )

                )

                chunk_number += 1

        return chunks
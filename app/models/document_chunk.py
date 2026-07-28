from dataclasses import dataclass


@dataclass
class DocumentChunk:

    # Source document
    document_name: str

    # Official law name
    law_name: str | None = None

    # Chapter or Title
    chapter: str | None = None

    # Article number
    article: str | None = None

    # Position inside the document
    chunk_number: int = 0

    # Legal text
    content: str = ""

    # Semantic embedding
    embedding: list[float] | None = None
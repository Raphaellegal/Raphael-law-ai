from dataclasses import dataclass


@dataclass
class DocumentChunk:
    document_name: str
    chunk_number: int
    content: str
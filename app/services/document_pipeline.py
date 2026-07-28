from app.services.document_loader import DocumentLoader
from app.services.legal_parser import LegalParser
from app.services.chunk_builder import ChunkBuilder


class DocumentPipeline:
    """
    Complete legal document processing pipeline.
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.parser = LegalParser()
        self.chunk_builder = ChunkBuilder()


    def process(
        self,
        relative_path: str,
        law_name: str
    ):

        text = self.loader.load_text(
            relative_path
        )

        law = self.parser.parse(
            text,
            law_name
        )

        chunks = self.chunk_builder.build(
            law
        )

        print("TOTAL CHUNKS:", len(chunks))

        if len(chunks) > 0:
            print("\nFIRST CHUNK:\n")
            print(chunks[0].content[:500])

        return chunks
from pathlib import Path

from app.services.pdf_reader import PDFReader


class DocumentLoader:
    """
    Loads legal documents from the legal_documents folder.
    """

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent.parent

        self.documents_folder = self.project_root / "legal_documents"

        self.pdf_reader = PDFReader()


    def load_text(self, relative_path: str) -> str:
        """
        Load a text or PDF document.
        """

        file_path = self.documents_folder / relative_path

        if not file_path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )


        if file_path.suffix.lower() == ".pdf":

            return self.pdf_reader.read(
                str(file_path)
            )


        return file_path.read_text(
            encoding="utf-8"
        )
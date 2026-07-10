from pathlib import Path


class DocumentLoader:
    """
    Loads legal documents from the legal_documents folder.
    """

    def __init__(self):
        self.project_root = Path(__file__).resolve().parent.parent.parent
        self.documents_folder = self.project_root / "legal_documents"

    def load_text(self, relative_path: str) -> str:
        """
        Load a text file from the legal_documents folder.
        """

        file_path = self.documents_folder / relative_path

        if not file_path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")

        return file_path.read_text(encoding="utf-8")
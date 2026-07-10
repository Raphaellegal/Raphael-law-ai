import os


class DocumentLoader:
    """
    Loads legal documents from files.
    """

    def load_text(self, file_path: str) -> str:
        """
        Load one text document.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read()
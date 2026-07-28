from pypdf import PdfReader


class PDFReader:
    """
    Extracts text from PDF legal documents.
    """

    def read(self, file_path: str) -> str:

        reader = PdfReader(file_path)

        text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)
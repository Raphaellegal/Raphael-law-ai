class ContextBuilder:
    """
    Builds AI context from legal document chunks.
    """

    def build(self, chunks):

        context = ""

        for chunk in chunks:

            context += (
                f"\n\n"
                f"Document: {chunk.document_name}\n"
                f"{chunk.content}"
            )

        return context.strip()
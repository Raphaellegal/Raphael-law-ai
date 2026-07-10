class ContextBuilder:
    """
    Builds AI context from legal document chunks.
    """

    def build(self, chunks):

        context = ""

        for chunk in chunks:
            context += (
                "\n\n"
                + chunk.content
            )

        return context.strip()
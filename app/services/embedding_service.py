from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _model = None

    def __init__(self):

        if EmbeddingService._model is None:

            print("Loading embedding model...")

            EmbeddingService._model = SentenceTransformer(
                "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            )

        self.model = EmbeddingService._model


    def create_embedding(self, text: str):

        return self.model.encode(
            text
        ).tolist()
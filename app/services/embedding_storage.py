import os
import pickle


class EmbeddingStorage:
    """
    Saves and loads processed legal chunks.
    """

    def __init__(self):
        self.file_path = "legal_documents/embeddings.pkl"


    def save(self, chunks):

        with open(
            self.file_path,
            "wb"
        ) as file:
            pickle.dump(
                chunks,
                file
            )


    def load(self):

        if not os.path.exists(self.file_path):
            return None

        with open(
            self.file_path,
            "rb"
        ) as file:
            return pickle.load(file)
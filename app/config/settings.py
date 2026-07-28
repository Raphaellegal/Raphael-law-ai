from app.config.languages import LANGUAGES



class Settings:
    """
    Global application settings.
    """

    def __init__(self):

        # Application information
        self.app_name = "Raphael Legal AI"
        self.version = "0.1.0"

        # Interface
        self.language = "en"
        self.available_languages = LANGUAGES

        # Legal documents
        self.documents_path = "legal_documents"

        # AI configuration (future)
        self.ai_provider = "none"

        # Development
        self.debug_mode = True


settings = Settings()
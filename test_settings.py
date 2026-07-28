from app.config.settings import settings


print("Application:", settings.app_name)
print("Version:", settings.version)
print("Language:", settings.language)
print("Documents:", settings.documents_path)
print("AI:", settings.ai_provider)
print("Debug:", settings.debug_mode)
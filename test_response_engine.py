from app.core.knowledge import initialize_knowledge
from app.core.legal_response_engine import LegalResponseEngine


initialize_knowledge()

engine = LegalResponseEngine()

context = engine.build_context(
    "Can my employer terminate my contract?"
)

print(context)
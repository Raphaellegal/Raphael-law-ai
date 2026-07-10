from app.core.knowledge import initialize_knowledge
from app.core.raphael_brain import RaphaelBrain


initialize_knowledge()

brain = RaphaelBrain()

answer = brain.think(
    "Can my employer terminate my contract?"
)

print(answer)
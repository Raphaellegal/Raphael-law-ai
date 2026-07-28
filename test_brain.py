from app.core.knowledge import initialize_knowledge
from app.core.raphael_brain import RaphaelBrain


initialize_knowledge()

brain = RaphaelBrain()

answer = brain.think(
    "ما هي شروط عقد العمل في تونس؟"
)

print(answer)
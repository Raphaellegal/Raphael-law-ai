from app.gui import start_gui
from app.core.knowledge import initialize_knowledge


if __name__ == "__main__":

    initialize_knowledge()

    start_gui()
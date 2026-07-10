import os

def ask_question(question: str) -> str:

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "legal_documents", "labor_code", "labor_code.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()

        # TEMPORARY: just return raw content + question context
        return f"""QUESTION:
{question}

---
LABOR CODE DATA (RAW):
{data[:800]}...
"""

    except Exception as e:
        return f"Error loading legal data: {str(e)}"
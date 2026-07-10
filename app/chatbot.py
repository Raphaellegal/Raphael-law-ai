from app.legal_engine import get_legal_response
from app.services.document_loader import load_documents
from app.document_search import search_documents
from app.response_builder import build_explanation

documents = load_documents()
print("Loaded documents:", documents.keys())

def start_chat():
    print("Raphael Legal Assistant started.")
    print("Type 'exit' to quit.\n")

    documents = load_documents()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Raphael: Goodbye 👋")
            break

        # 1. Search documents FIRST
        results = search_documents(user_input, documents)

        if results:
            answer = build_explanation(results)

            print("\nRaphael:")
            print(answer)
            continue

        # 2. Then fallback to legal engine
        response = get_legal_response(user_input)

        if response:
            print("Raphael:", response)
        else:
            print("Raphael: I couldn't find anything yet.")
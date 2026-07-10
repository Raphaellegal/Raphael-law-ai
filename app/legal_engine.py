from data.legal_data import LEGAL_TOPICS


def get_legal_response(message: str):
    message = message.lower()

    for topic_key, topic_data in LEGAL_TOPICS.items():
        for keyword in topic_data["keywords"]:
            if keyword in message:
                return f"{topic_data['title']}: {topic_data['definition']}"

    return None
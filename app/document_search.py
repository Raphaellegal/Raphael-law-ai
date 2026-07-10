def search_documents(query, documents):
    query = query.lower()
    query_words = set(query.split())

    results = []

    for filename, content in documents.items():
        sentences = content.split(".")

        scored = []

        for sentence in sentences:
            sentence_clean = sentence.strip()
            sentence_words = set(sentence_clean.lower().split())

            if not sentence_clean:
                continue

            # score = number of matching words
            score = len(query_words.intersection(sentence_words))

            if score > 0:
                scored.append({
                    "sentence": sentence_clean,
                    "score": score
                })

        # sort by importance
        scored.sort(key=lambda x: x["score"], reverse=True)

        if scored:
            results.append({
                "file": filename,
                "top_sentences": [s["sentence"] for s in scored[:3]]
            })

    return results
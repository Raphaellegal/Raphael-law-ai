def build_explanation(results):
    if not results:
        return None

    final_answer = []

    for r in results:
        final_answer.append(f"From {r['file']}:")

        for sentence in r["top_sentences"]:
            final_answer.append("- " + sentence)

    return "\n".join(final_answer)
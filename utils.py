from minsearch import Index


def build_index(documents):
    index = Index(
        text_fields=["question", "answer"],
    )
    index.fit(documents)
    return index
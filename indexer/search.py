from collections import Counter
from storage.storage import get_detail_document

def search(query, tfidf_index, top_k=10):
    
    query_words = query.lower().split()

    scores = Counter()

    for word in query_words:
        if word in tfidf_index:
            scores.update(tfidf_index[word])

    if not scores:
        return []

    return scores.most_common(top_k)



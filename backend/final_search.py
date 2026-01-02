from storage.storage import get_detail_document
from indexer.search import search


def final_search(query, tfidf_index, top_k=10):
    ranked_docs = search(query, tfidf_index, top_k)

    results = []

    for doc_id, score in ranked_docs:
        detail = get_detail_document(doc_id)
        if detail:
            title, url = detail
            results.append({
                "title": title,
                "url": url,
                "score": score
            })

    return results

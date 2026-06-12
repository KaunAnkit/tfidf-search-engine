from flask import Flask, request, jsonify
import os
from backend.final_search import final_search
from indexer.score_saver import load_index

from storage.storage import get_detail_document
from recommender.content_based import build_doc_vector, get_similar_docs

from storage.storage import get_all_titles

app = Flask(__name__)

print("Loading TF-IDF index...")
tfidf_index = load_index()
print("TF-IDF index loaded")

print("Loading titles...")

titles = get_all_titles()

print(f"Loaded {len(titles)} titles")

doc_set = set()

for postings in tfidf_index.values():
    doc_set.update(postings.keys())

print("Documents:", len(doc_set))
print("Terms:", len(tfidf_index))
print(next(iter(tfidf_index.items())))

@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "query parameter 'q' is required"}), 400

    results = final_search(query, tfidf_index, top_k=10)

    return jsonify(results)

# @app.route("/recommend")
# def recommend():

#     doc_id = request.args.get("doc_id")

#     if not doc_id:
#         return jsonify({"error": "doc_id parameter is required"}), 400
    
#     try:
#         top_n = min(
#             max(int(request.args.get("n", 5)), 1),
#             20
#         )
#     except ValueError:
#         top_n = 5

#     try:
#         recs = get_similar_docs(doc_id, doc_matrix, doc_ids, top_n=top_n)
#     except ValueError:
#         return jsonify({"error": f"doc_id not found in index: {doc_id}"}), 404
    
#     enriched = []
#     for r in recs:
#         detail = get_detail_document(r["doc_id"])   
#         enriched.append({
#             "doc_id": r["doc_id"],
#             "score":  r["score"],
#             "title":  detail[0] if detail else r["doc_id"],
#             "url":    detail[1] if detail else None,
#         })
 
#     return jsonify({"query_doc_id": doc_id, "recommendations": enriched})



@app.route("/")
def home():
    return {
        "service": "TF-IDF Search Service",
        "status": "running"
    }

@app.route("/suggest")
def suggest():

    q = request.args.get("q", "").lower().strip()

    if len(q) < 2:
        return jsonify([])

    matches = []

    for title in titles:

        title_lower = title.lower()

        score = 0

        if title_lower.startswith(q):
            score = 100

        elif any(
            word.startswith(q)
            for word in title_lower.split()
        ):
            score = 50

        elif q in title_lower:
            score = 10

        if score > 0:
            matches.append({
                "title": title,
                "score": score
            })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return jsonify(matches[:8])





if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

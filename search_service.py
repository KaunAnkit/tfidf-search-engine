from flask import Flask, request, jsonify
import os
from backend.final_search import final_search
from indexer.score_saver import load_index

app = Flask(__name__)

print("Loading TF-IDF index...")
tfidf_index = load_index()
print("TF-IDF index loaded")


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


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )

from backend.final_search import final_search
from indexer.tfidf_indexer import build_tidf_indexer
from indexer.score_saver import load_index


def main():
    print("Loading search index...")
    tfidf_index = load_index()

    if tfidf_index is None:
        print("Index not found. Building index (one-time)...")
        tfidf_index = build_tidf_indexer()
        print("Index built and saved.")

    print("Index ready.\n")

    while True:
        query = input("Search (type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        results = final_search(query, tfidf_index, top_k=10)

        if not results:
            print("No results found.\n")
            continue

        for i, r in enumerate(results, 1):
            print(f"{i}. {r['title']}")
            print(f"   {r['url']}")
            print(f"   score: {r['score']:.4f}\n")


if __name__ == "__main__":
    main()

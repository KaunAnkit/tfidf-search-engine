# Retrieval — TF-IDF Search Engine

A custom search engine built from scratch using classical Information Retrieval techniques. Retrieval crawls real-world websites, indexes content using TF-IDF, and delivers ranked search results through a web interface and REST API — no LLMs, no vector databases.

---

## Live Stats

| Metric | Value |
|---|---|
| Indexed webpages | ~1,400 |
| Unique terms | ~253,000 |
| Autocomplete | Real-time |
| Deployment target | Render (512 MB free tier) |

---

## Features

**Search Engine Core**
- Web crawler with breadth-first traversal
- HTML parsing and clean text extraction
- Text normalization and tokenization
- Inverted index generation
- TF-IDF ranking
- Persistent index storage

**Search Experience**
- Ranked search results with match score visualization
- Real-time autocomplete suggestions
- Domain-aware result display
- Fast retrieval via precomputed indexes

**Backend Infrastructure**
- Python search service
- MongoDB document storage
- Node.js API gateway
- REST API endpoints

---

## Architecture

```
retrieval/
├── crawler/
│   ├── crawl_loop.py        # Orchestrates crawl sessions
│   └── crawler.py           # BFS traversal, link extraction, deduplication
│
├── indexer/
│   ├── tokenizer.py         # Text normalization and tokenization
│   ├── tfidf.py             # TF-IDF computation
│   ├── search.py            # Query execution and result ranking
│   └── score_saver.py       # Serializes index to disk
│
├── storage/
│   └── storage.py           # MongoDB document persistence
│
├── backend/
│   └── final_search.py      # Python search service entrypoint
│
└── server/
    ├── src/server.js         # Express API gateway
    └── ...                  # MongoDB integration, routing
```

---

## How It Works

### 1. Crawling

The crawler begins from a set of seed URLs and performs **breadth-first traversal** across the web. For each page it visits, it:

- Downloads the raw HTML
- Extracts and cleans visible text
- Discovers and enqueues outbound links
- Deduplicates visited URLs
- Stores documents in MongoDB for indexing

### 2. Indexing

Collected documents are tokenized and transformed into an **inverted index** — a mapping from every unique term to the documents it appears in, along with a precomputed TF-IDF score:

```python
{
    "python": {
        "doc_1": 0.42,
        "doc_2": 0.18
    }
}
```

The index is serialized to disk for fast reloading without re-computation.

### 3. Ranking (TF-IDF)

Each query term is looked up in the inverted index. Documents are ranked by the **sum of TF-IDF scores** across all query terms.

**Term Frequency (TF)**
```
TF = Occurrences of term in document / Total terms in document
```

**Inverse Document Frequency (IDF)**
```
IDF = log(Total Documents / Documents Containing Term)
```

**Final Score**
```
Score = TF × IDF
```

Documents with the highest aggregated scores are returned first.

### 4. Autocomplete

The suggestion engine matches typed prefixes against indexed term data in real time — without loading the full vocabulary into memory.

```
Input: "pyth"
→ Python Tutorial
→ Python Documentation

Input: "mach"
→ Machine Learning Tutorial
→ Machine Learning with Python
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- MongoDB (local or Atlas)

### Installation

```bash
git clone https://github.com/KaunAnkit/tfidf-search-engine.git
cd tfidf-search-engine
pip install -r requirements.txt
```

### Running the Crawler

```bash
python run_crawler.py
```

### Starting the Search Service

```bash
python search_service.py
```

### Starting the Node API

```bash
cd server
npm install
node src/server.js
```

---

## API Reference

### Search

```http
GET /search?q={query}
```

**Example**
```
GET /search?q=python
```

**Response**
```json
[
  {
    "title": "Python Tutorial",
    "url": "https://example.com",
    "score": 0.31
  }
]
```

### Autocomplete Suggestions

```http
GET /suggest?q={prefix}
```

**Example**
```
GET /suggest?q=pyth
```

**Response**
```json
[
  {
    "title": "Python Tutorial",
    "score": 100
  }
]
```

---

## Engineering Challenges

| Challenge | Solution |
|---|---|
| Scaling from 200 → 1,400 pages | Incremental crawl loop with persistent state |
| 512 MB Render memory limit | Lazy index loading, disk-backed serialization |
| 253k+ term vocabulary | Prefix-based autocomplete without full in-memory load |
| Classical IR without embeddings | Pure TF-IDF with precomputed inverted index |

---

## Author

**Ankit Jha**
GitHub: [@KaunAnkit](https://github.com/KaunAnkit)


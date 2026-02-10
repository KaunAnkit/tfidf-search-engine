# TF-IDF Based Search Engine

## Overview

This project implements classical information retrieval from scratch. It crawls real-world websites, extracts content, builds an inverted index with TF-IDF scoring, and enables efficient document search without relying on machine learning.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Node.js](https://img.shields.io/badge/Node.js-v16.14.0-green)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- Web crawler with breadth-first traversal and depth control
- HTML parsing and text normalization
- SQLite-based document storage
- Inverted index with TF-IDF ranking
- Persistent index storage for fast retrieval
- Command-line search interface
- Web-based search UI
- Node.js API server with MongoDB integration

## Architecture
```
crawler/     → Web crawling, HTML parsing, text cleaning
indexer/     → Tokenization, TF-IDF computation, index persistence
storage/     → SQLite database layer
backend/     → Search orchestration
server/      → Node.js/Express API with MongoDB
```

## Installation
```bash
git clone https://github.com/KaunAnkit/tfidf-search-engine.git
cd tfidf-search-engine
pip install -r requirements.txt
```

## Usage

### 1. Crawl and index documents
```bash
python run_crawler.py
```

### 2. Search via CLI
```bash
python cli.py
```

### 3. Run the search service
```bash
python search_service.py
```

### 4. Optional: Sync with MongoDB
```bash
# Configure .env with MongoDB connection string
python send_to_node.py

# Start Node.js server
cd server
npm install
node src/server.js
```

## How It Works

**Crawling**: BFS traversal starting from seed URLs, extracting text and links while avoiding duplicates.

**Indexing**: Tokenizes documents, builds an inverted index mapping terms to documents with frequency counts.

**Ranking**: Computes TF-IDF scores where:
- TF = term frequency in document / total terms in document
- IDF = log(total documents / documents containing term)
- Score = TF × IDF

**Search**: Aggregates TF-IDF scores across query terms and returns ranked results.

## Configuration

Modify seed URLs in `run_crawler.py` to crawl different domains. Adjust `max_pages` and `max_depth` to control crawl scope.

## Future Enhancements

- Stopword filtering and stemming
- PageRank-style authority scoring
- Semantic search with embeddings
- Query expansion and spell correction
- Evaluation metrics (precision, recall, MAP)

## License

MIT License - see LICENSE file for details.

## Author

Ankit Jha  
[GitHub](https://github.com/KaunAnkit)

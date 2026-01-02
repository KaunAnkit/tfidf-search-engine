# TF-IDF Based Search Engine

A search engine built from scratch that crawls real-world websites, indexes documents using an inverted index and TF-IDF scoring, and provides fast keyword-based search through a command-line interface.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Folder Structure](#folder-structure)
- [Indexing & Ranking](#indexing--ranking)
- [Design Decisions](#design-decisions)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Author](#author)

---

## Project Overview

This project implements a **classical information retrieval search engine** from scratch.  
It crawls websites, extracts and cleans text content, builds an inverted index, computes TF-IDF scores for ranking, and allows users to search documents via a CLI.

> ⚠️ This project focuses on **statistical IR (TF-IDF)**, not machine learning.  
> Semantic and ML-based ranking are listed as future extensions.

---

## Features

- ✅ Web crawler with BFS traversal and depth control
- ✅ HTML parsing and text cleaning
- ✅ SQLite-based document storage
- ✅ Inverted index construction
- ✅ TF-IDF scoring for relevance ranking
- ✅ Persisted index for fast startup
- ✅ Command-line interface (CLI) search
- ✅ Modular and extensible architecture

---

## How It Works

### 1️⃣ Crawling
- Starts from seed URLs
- Crawls pages using breadth-first search (BFS)
- Extracts visible text and outgoing links
- Avoids duplicate URLs

### 2️⃣ Indexing
- Tokenizes cleaned text
- Builds an inverted index (`word → {doc_id: frequency}`)
- Computes TF-IDF scores
- Persists index to disk for reuse

### 3️⃣ Searching
- Loads persisted index
- Tokenizes user query
- Aggregates TF-IDF scores
- Returns ranked documents

---

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/KaunAnkit/tfidf-search-engine.git
cd tfidf-search-engine
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

### Initialize database and crawl data

```bash
python run_crawler.py
```

### Start the CLI search engine

```bash
python cli.py
```

### Example

```
Search (type 'exit' to quit): cascade
1. CSS-Tricks - A Website About Making Websites
   https://css-tricks.com
   score: 0.0062


Search (type 'exit' to quit): python
1. 3.14.2 Documentation
   https://docs.python.org
   score: 0.1335

2. Python Tutorials – Real Python
   https://realpython.com
   score: 0.0765

3. freeCodeCamp Programming Tutorials: Python, JavaScript, Git & More
   https://www.freecodecamp.org/news
   score: 0.0185

4. Machine Learning Mastery
   https://machinelearningmastery.com
   score: 0.0080

5. scikit-learn: machine learning in Python — scikit-learn 1.8.0 documentation
   https://scikit-learn.org/stable
   score: 0.0067

6. FastAPI
   https://fastapi.tiangolo.com
   score: 0.0058

7. pandas documentation — pandas 2.3.3 documentation
   https://pandas.pydata.org/docs
   score: 0.0044

8. AWS Blogs - Cloud news & innovation | Amazon Web Services (AWS)
   https://aws.amazon.com/blogs
   score: 0.0039

9. Engineering at Meta - Engineering at Meta Blog
   https://engineering.fb.com
   score: 0.0027

10. Andrej Karpathy blog
   https://karpathy.github.io
   score: 0.0026
```

---

## Folder Structure

```
tfidf-search-engine/
│
├── cli.py          # Command-line interface
├── run_crawler.py  # Script to initialize database and run crawler
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
├── backend/        # Search orchestration
├── crawler/        # Crawling, parsing, cleaning
├── indexer/        # Tokenization, TF, IDF, TF-IDF indexing
├── storage/        # SQLite database access
└── data/           # Database and persisted index (ignored in git)
```

---

## Indexing & Ranking

### TF-IDF Formula

**Term Frequency (TF)**

```
TF = (count of term in document) / (total words in document)
```

**Inverse Document Frequency (IDF)**

```
IDF = log(total_documents / documents_containing_term)
```

**TF-IDF Score**

```
TF-IDF = TF × IDF
```

Documents are ranked based on cumulative TF-IDF scores for query terms.

---

## Design Decisions

- Offline indexing, online querying for performance
- Persisted index to avoid recomputation
- SQLite used for simplicity and reliability
- Modular design to allow future extensions
- No ML dependency in core ranking logic

---

## Future Improvements

- Stopword removal and stemming
- Domain-based ranking
- Page importance scoring
- Semantic search with embeddings
- Web-based frontend
- Precision / Recall evaluation metrics

---

## License

This project is licensed under the MIT License.

---

## Author

Ankit Jha  
GitHub: KaunAnkit

⭐ If you find this project useful, consider starring the repository!
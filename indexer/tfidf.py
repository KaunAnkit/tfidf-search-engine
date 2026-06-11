from indexer.tokenizer import count_tokenizer, tokenizer
from storage.storage import get_all_documents

from collections import defaultdict, Counter
import math

# Cache to avoid recomputing
_inverted_index_cache = None
_doc_lengths_cache = None

def tfidf(word, doc_id):
    global _inverted_index_cache, _doc_lengths_cache
    
    if _inverted_index_cache is None:
        _inverted_index_cache = count_tokenizer()
    if _doc_lengths_cache is None:
        _doc_lengths_cache = compute_doc_lengths()
    
    inverted_index = _inverted_index_cache
    doc_lengths = _doc_lengths_cache

    total_docs = len(doc_lengths)

    df = len(inverted_index[word])
    tf = inverted_index[word][doc_id] / doc_lengths[doc_id]

    idf = math.log(total_docs / df)

    return tf * idf

def compute_doc_lengths():
    data = get_all_documents()
    doc_lengths = {}

    for doc_id, text in data:
        tokens = tokenizer(text)
        doc_lengths[doc_id] = len(tokens)

    return doc_lengths




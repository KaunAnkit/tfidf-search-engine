from indexer.tokenizer import count_tokenizer, tokenizer
from storage.storage import get_all_documents

from collections import defaultdict, Counter
import math


def tfidf(word, doc_id):
    inverted_index = count_tokenizer()
    doc_lengths = compute_doc_lengths()

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




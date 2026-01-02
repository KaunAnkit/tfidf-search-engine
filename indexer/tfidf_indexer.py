from collections import defaultdict
from indexer.tokenizer import count_tokenizer
from indexer.tfidf import tfidf
from indexer.score_saver import save_index


def build_tidf_indexer():
    freq_index = count_tokenizer()
    tfidf_index = defaultdict(dict)

    for word, doc_dict in freq_index.items():
        for doc_id in doc_dict:
            tfidf_index[word][doc_id] = tfidf(word, doc_id)

    save_index(tfidf_index)

    return tfidf_index

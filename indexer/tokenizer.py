from storage.storage import get_all_documents
from collections import defaultdict, Counter
import re

def tokenizer(text): 

    text = text.lower()
    tokens = re.findall(r"\b[a-z0-9]+\b", text)
    return tokens

def count_tokenizer():

    data = get_all_documents()

    inverted_index = defaultdict(dict)

    for doc_id , text in data:
        
        tokens = tokenizer(text)
        word_counts = Counter(tokens)

        for word, freq in word_counts.items():
            inverted_index[word][doc_id] = freq

    return inverted_index


  



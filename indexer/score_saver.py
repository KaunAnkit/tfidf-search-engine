import pickle
import os

INDEX_PATH = "data/tfidf_index.pkl"


def save_index(index):
    with open(INDEX_PATH, "wb") as f:
        pickle.dump(index, f)


def load_index():
    if not os.path.exists(INDEX_PATH):
        return None

    with open(INDEX_PATH, "rb") as f:
        return pickle.load(f)

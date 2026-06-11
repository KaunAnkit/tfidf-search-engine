import numpy as np
import math

def build_doc_vector(tfid_index:dict):

    vocab = sorted(tfid_index)

    doc_id_set = set()

    for x in tfid_index.values():

        doc_id_set.update(x.keys())

    doc_ids = sorted(doc_id_set)


    if not doc_ids or not vocab:

        return np.zeros((0,0), dtype=np.float32), [],[]
    
    vocab_idx = {}

    for i,ids in enumerate(vocab):

        vocab_idx[ids] = i

    doc_idx = {}

    for i,ids in enumerate(doc_ids):
        
        doc_idx[ids] = i

    matrix = np.zeros((len(doc_ids),len(vocab)),dtype=np.float32,)
    

    for x,y in tfid_index.items():

        col = vocab_idx[x]

        for doc_id,score in y.items():

            row = doc_idx[doc_id]
            matrix[row,col] = score


    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0          
    matrix = matrix / norms

    return matrix,doc_ids,vocab


def get_similar_docs(query_doc_id,matirx,doc_ids,top_n=5,min_score=0.05):

    if query_doc_id not in doc_ids:

        raise ValueError(f"doc_id {doc_ids} not found index mai dekhlo ab" )

    doc_lookup = {
        doc_id: i
        for i, doc_id in enumerate(doc_ids)
        }
    
    idx = doc_lookup[query_doc_id]
    
    query_vec = matirx[idx]

    scores = matirx.dot(query_vec)

    scores[idx] = -0.1

    candidate_count = min(top_n + 1, len(scores))
    top_indices = np.argpartition(scores, -candidate_count)[-candidate_count:]
    top_indices = top_indices[np.argsort(scores[top_indices])[::-1]]

    results = []
    for i in top_indices:
        score = float(scores[i])
        if score < min_score:
            continue
        results.append({"doc_id": doc_ids[i], "score": round(score, 4)})
        if len(results) >= top_n:
            break
 
    return results
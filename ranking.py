import numpy as np

def rank_by_tfidf(query, index_dict):
    if len(query) == 1: # if single term query
        doc_dict = index_dict[query]
        sorted_docs = sorted(doc_dict.items(), key=lambda item:item[1][2])
        return sorted_docs

    elif len(query) > 1:
        pass
        

def cosine_similarity(q,d):
    # q is a vector of the tf-idf of each term in the query
    # d is a vector of the tf-idf of each term in the document
    return (np.dot(q,d)) / (np.sqrt(np.dot(q,q)) * np.sqrt(np.dot(d,d)))

q = [1.09, 2.00]
d1 = [1.75, 2.93]
d2 = [3.49, 2.92]
d3 = [1.09, 1.13]

print(cosine_similarity(q,d1))
print(cosine_similarity(q,d2))
print(cosine_similarity(q,d3))
def rank_by_tfidf(query, index_dict):
    if len(query) == 1: # if single term query
        doc_dict = index_dict[query]
        sorted_docs = sorted(doc_dict.items(), key=lambda item:item[1][2])
        return sorted_docs

    elif len(query) > 1:
        

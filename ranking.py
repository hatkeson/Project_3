import numpy as np

def ranked_results(query, index_dict):
    # Assuming query length has to be > 0
    if len(query) == 1: # if single term query
        doc_dict = index_dict[query]
        sorted_docs = sorted(doc_dict.items(), key=lambda item:item[1][2], reverse=True)
        return sorted_docs

    elif len(query) > 1:
        str_list = query.split()
        d_vector = []
        q_vector = []
        result_dict = {} # same as index_dict, but result_dict[word][doc][2] is scoring instead of tf-idf score
        # Calculate d and q of each term in query
        # TODO: remember type of the word
        # get q_vector first
        for word in str_list:
            # add word entry in index_dict to result_dict
            result_dict[word] = index_dict[word]
            # q value
            q_value = ((1 + np.log10(str_list.count(word))) * (np.log10(36496) / (len(index_dict[word]) + 1)))
            q_vector.append(q_value)

        # get d_vector for each doc, then calculate cosine similarity for each doc => scoring
        for word in str_list:
            d_vector.clear()
            doc_list = list(result_dict[word])
            visited = set()
            for doc in doc_list:
                for sub_word in str_list:
                    if sub_word != word \
                            and sub_word in result_dict \
                            and doc in result_dict[sub_word] \
                            and doc not in visited:
                        d_vector.append(index_dict[sub_word][doc][2])
                result_dict[word][doc][2] = cosine_similarity(q_vector, d_vector)
                visited.add(doc)



        

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
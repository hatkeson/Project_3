import numpy as np

def ranked_results(query, index_dict):
    # Assuming query length has to be > 0
    if len(query) == 1: # if single term query
        doc_dict = index_dict[query]
        sorted_docs = sorted(doc_dict.items(), key=lambda item:item[1][2], reverse=True)
        return sorted_docs

    elif len(query) > 1:
        str_set = set(query.split())
        d_vector = []
        q_vector = []
        doc_dict = {}   # dictionary of resulting docs
        doc_set = set() # set of resulting docs
        # Calculate d and q of each term in query
        # TODO: remember type of the word
        # get q_vector first
        for word in str_set:
            for doc in list(index_dict[word]):
                doc_set.add(doc)
            # q value
            q_value = ((1 + np.log10(query.split().count(word))) * (np.log10(36496) / (len(index_dict[word]) + 1)))
            q_vector.append(q_value)

        # get d_vector for each doc, then calculate cosine similarity for each doc => scoring
        for doc in doc_set:
            for word in str_set:
                if word in index_dict and doc in index_dict[word]:
                    d_vector.append(index_dict[word][doc][2])
                else:
                    d_vector.append(0)
            doc_dict[doc] = cosine_similarity(q_vector, d_vector)
        return sorted(doc_dict.items(), key=lambda item:item, reverse=True)




        # i = 0   # i is the order of the word in the query (to make sure q and d align)
        # for word in str_set:
        #     d_vector.clear()
        #     doc_list = list(result_dict[word])
        #     visited = set()
        #     for doc in doc_list:
        #         for sub_word in str_set:
        #             if sub_word != word and sub_word in result_dict:
        #                 if doc not in visited and doc in result_dict[sub_word]:
        #                     d_vector.append(index_dict[sub_word][doc][2])
        #                 elif doc not in visited and doc not in result_dict[sub_word]:
        #                     d_vector.append(0)
        #             elif sub_word != word and sub_word not in result_dict:
        #                 d_vector.append(0)
        #
        #         result_dict[word][doc][2] = cosine_similarity(q_vector, d_vector)
        #         visited.add(doc)



        

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
import numpy as np
import copy

def ranked_results(query, index_dict):
    # Assuming query length has to be > 0
    if ' ' in query:
        str_set = set(query.split())
        d_vector = []
        q_vector = []
        doc_dict = {}   # dictionary of resulting docs
        doc_set = set() # set of resulting docs
        # Calculate d and q of each term in query
        # TODO: remember type of the word for scoring [DONE]
        # TODO: ^ how would type be incorporated in queries with >= 2 terms?
        # TODO: confirm if formula for q value is correct
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
                    multiplier = 1
                    if index_dict[word][doc][1] == 2:
                        multiplier = 1.5
                    elif index_dict[word][doc][1] == 3:
                        multiplier = 2
                    elif index_dict[word][doc][1] == 4:
                        multiplier = 2.5
                    d_vector.append(index_dict[word][doc][2] * multiplier)
                else:
                    d_vector.append(0)
            doc_dict[doc] = cosine_similarity(q_vector, d_vector)
            d_vector.clear()

        return sorted(doc_dict.items(), key=lambda item:item[1], reverse=True)


def cosine_similarity(q,d):
    # q is a vector of the tf-idf of each term in the query
    # d is a vector of the tf-idf of each term in the document
    print(q)
    print(d)
    return (np.dot(q,d)) / (np.sqrt(np.dot(q,q)) * np.sqrt(np.dot(d,d)))

# q = [1.09, 2.00]
# d1 = [1.75, 2.93]
# d2 = [3.49, 2.92]
# d3 = [1.09, 1.13]
#
# print(cosine_similarity(q,d1))
# print(cosine_similarity(q,d2))
# print(cosine_similarity(q,d3))
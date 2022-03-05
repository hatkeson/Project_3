import numpy as np
import copy
import nltk

# Used for calculating query score by unigrams
def ranked_results_by_unigrams(query, index_dict):
    # Assuming query length has to be > 0
    if ' ' in query:
        str_set = set(query.split())
        d_vector = []
        q_vector = []
        doc_dict = {}   # dictionary of resulting docs: keys = doc, value = score
        doc_set = set() # set of resulting docs
        # Calculate d and q of each term in query
        # get q_vector first
        for word in str_set:
            if word in index_dict:
                for doc in list(index_dict[word]):
                    doc_set.add(doc)    # Add to set => I have visited this doc
                # q value
                q_value = ((1 + np.log10(query.split().count(word))) * (np.log10(36496) / (len(index_dict[word]) + 1)))
                q_vector.append(q_value)
            else:
                q_vector.append(0)

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

    else:    # if ' ' is not query => single term queries
        # tf-idf with unigram
        if query in index_dict:
            doc_dict = copy.deepcopy(index_dict[query])
            doc_list = list(doc_dict)
            # modify tf-idf score based on type of text
            for doc in doc_list:
                multiplier = 1
                if doc_dict[doc][1] == 2:
                    multiplier = 1.5
                elif doc_dict[doc][1] == 3:
                    multiplier = 2
                elif doc_dict[doc][1] == 4:
                    multiplier = 2.5
                doc_dict[doc][2] = doc_dict[doc][2] * multiplier
            return sorted(doc_dict.item(), key=lambda item:item[1], reverse=True)
        else:
            return []

# Used for 2+-term queries
def ranked_results_by_bigrams(query, bindex_dict):
    # get bigrams from query
    temp_bigrams = list(nltk.ngrams(nltk.word_tokenize(query), 2))
    bigrams_list = [' '.join(bigram) for bigram in temp_bigrams]

    bigram_set = set(bigrams_list)
    d_vector = []
    q_vector = []
    doc_dict = {}
    doc_set = set()
    # Calculate d and q of each bigram in query
    # get q_vector first
    for bigram in bigram_set:
        if bigram in bindex_dict:
            for doc in list(bindex_dict[bigram]):
                doc_set.add(doc) # I have visited this doc
            # q value
            q_value = ((1 + np.log10(bigrams_list.count(bigram))) * (np.log10(36354) / (len(bindex_dict[bigram]) + 1)))
            q_vector.append(q_value)
        else:
            q_vector.append(0)

    # get d vector for each doc, then calculate cosine similarity for each doc => scoring
    for doc in doc_set:
        for bigram in bigram_set:
            if bigram in bindex_dict and doc in bindex_dict[bigram]:
                multiplier = 3
                if bindex_dict[bigram][doc][1] == 2:
                    multiplier = 3.5
                elif bindex_dict[bigram][doc][1] == 3:
                    multiplier = 4
                elif bindex_dict[bigram][doc][1] == 4:
                    multiplier = 4.5
                d_vector.append(bindex_dict[bigram][doc][2] * multiplier)
            else:
                d_vector.append(0)
        doc_dict[doc] = cosine_similarity(q_vector, d_vector)
        d_vector.clear()

    return sorted(doc_dict.items(), key=lambda item:item[1], reverse=True)



def cosine_similarity(q,d):
    # q is a vector of the tf-idf of each term in the query
    # d is a vector of the tf-idf of each term in the document
    return (np.dot(q,d)) / (np.sqrt(np.dot(q,q)) * np.sqrt(np.dot(d,d)))
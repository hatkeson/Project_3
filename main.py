from enum import unique
from operator import inv
import sys
import json
from bs4 import BeautifulSoup
#from index_constructor import InvertedIndex
import copy
import nltk

if __name__ == "__main__":
    pass
    # get directory of the webpages file, feed to constructor
    # inv_idx = InvertedIndex()
    # inv_idx.read_corpus(sys.argv[1])
    # inv_idx.calculate_tf_idf()
    # inv_idx.write_to_json()

    # # Get index dict from json file
    # with open('bigram_index_text_file.json') as file:
    #     #index = json.load(file)
    #     index_dict = json.load(file)



    # with open('D:\\121 Project 3\webpages\WEBPAGES_RAW\\bookkeeping.json') as b:
    #     bookkeeping = json.load(b)
    #
    # # unique documents
    # unique_words = 0
    # unique_docs = set()
    # for word in index_dict:
    #     unique_words += 1
    #     for doc in index_dict[word]:
    #         unique_docs.add(doc)
    #
    # print('Searching ' + str(unique_words) + ' words in ' + str(len(unique_docs)) + ' documents.')

    # print('Size of index (KB): ' + str(sys.getsizeof(index_dict) / 1000))

    # #print(index_dict['mondego'])
    # doc_dict = copy.deepcopy(index_dict['mondego'])
    # #sorted_docs = sorted(doc_dict.items(), key=lambda item: item[1][2], reverse=True)
    # for doc in list(doc_dict):
    #     doc_dict[doc][2] = doc_dict[doc][2] + 10
    # print(doc_dict)
    # print(index_dict['mondego'])

    # bigrams = list(nltk.ngrams(nltk.word_tokenize("hi hello there hey"), 2))
    # print("before: ")
    # print(bigrams)
    # bigrams_list = [' '.join(bigram) for bigram in bigrams]
    # print("After: ")
    # print(bigrams_list)

    # Get user input
    # user_quit = False
    # while not user_quit:
    #     query = input("Enter query: ")
    #
    #     # Exit word
    #     if query == "close search":
    #         user_quit = True
    #
    #     lower_query = query.lower()
    #
    #     # We have index, now we can look up the query/word on the index
    #     # print(index_dict[lower_query])
    #     if not user_quit:
    #         result_count = 0
    #         for result in index_dict[lower_query]:
    #             if result in bookkeeping and result_count < 20:
    #                 print(bookkeeping[result])
    #                 result_count += 1
    #         print(str(result_count) + ' results.')

# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)
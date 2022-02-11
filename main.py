from operator import inv
import sys
import json
from bs4 import BeautifulSoup
from index_constructor import InvertedIndex

if __name__ == "__main__":

    # get directory of the webpages file, feed to constructor
    # inv_idx = InvertedIndex()
    # inv_idx.read_corpus(sys.argv[1])
    # inv_idx.calculate_tf_idf()
    # inv_idx.write_to_json()

    # Get index dict from json file
    with open('index_text_file.json') as file:
        index = json.load(file)
        index_dict = json.loads(index)
        print(index_dict["informatics"])


    # # Get user input
    # while True:
    #     query = input("Enter query: ")
    #     print(query)
    #
    #     # We have index, now we can look up the query/word on the index
    #     print(index[query])

# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)
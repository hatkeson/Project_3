from operator import inv
import sys
from bs4 import BeautifulSoup
from index_constructor import InvertedIndex

if __name__ == "__main__":

    # get directory of the webpages file, feed to constructor
    inv_idx = InvertedIndex()
    inv_idx.read_corpus(sys.argv[1])
    inv_idx.calculate_tf_idf()
    inv_idx.write_to_json()


# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)
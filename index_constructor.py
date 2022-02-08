import nltk

# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)

def remove_stopwords():
    pass
def lemmatize():
    pass
def get_tf_idf():
    # tf = (count of term in document) / (total word count of document)
    # idf = (total number of documents in corpus) / (count of documents where term appears)
    # tf-idf = tf * idf
    pass


class InvertedIndex():
    def __init__(self):
        self.stopwords = []
        self.document_count = 0
        self.index = {} # only for inverted index
        self.title_index = {}
        self.heading_index = {}
        self.bold_index = {}

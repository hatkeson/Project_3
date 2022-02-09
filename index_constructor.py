import nltk
import json
from bs4 import BeautifulSoup

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


class InvertedIndex:
    def __init__(self):
        self.document_count = 0
        self.index = {} # only for inverted index
        self.title_index = {}
        self.heading_index = {}
        self.bold_index = {}

        self.stopwords = []
        with open('stopwords.txt') as file:
            for line in file:
                self.stopwords.append(line.rstrip())


    def read_corpus(self, corpus_path):
        # get the bookkeeping file
        print(corpus_path)
        with open(corpus_path + '\\bookkeeping.json') as f:
            bookkeeping = json.load(f)

        # for each entry in bookkeeping, navigate to the folder and then file, and read it with BS
        # first number is folder
        # second number is file
        for key in bookkeeping:
            print(key)
            folder_file = key.split('/')
            if folder_file[0] != '0': # hardcoded limit, remove when ready for full corpus
                break
            print(bookkeeping[key])
            with open(corpus_path + '\\' + folder_file[0] + '\\' + folder_file[1], 'rb') as f:
                page = BeautifulSoup(f)
                title = page.find('title')
                heading_1 = page.find('h1')
                heading_2 = page.find('h2')
                heading_3 = page.find('h3')
                bold = page.find('b')
            if title:
                print(title.get_text())
            if heading_1:
                print(heading_1.get_text())
            if heading_2:
                
            if heading_3:
            if bold:


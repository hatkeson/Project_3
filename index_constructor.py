from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from string import punctuation
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

            # tokenize
            # Whitespace tokenizer - keep contractions because they're in stopwords
            tokenizer = WhitespaceTokenizer()
            text_tokens = tokenizer.tokenize(page.get_text())

            # lemmatize - must strip leading and trailing punctuation because whitespace
            # tokenizer leaves them in
            lemmatizer = WordNetLemmatizer()
            text_tokens_len = len(text_tokens)
            for i in range(0, text_tokens_len):
                text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

            # add to inverted index
            for word in text_tokens:
                if word not in self.stopwords:
                    if word in self.index and key in self.index[word]: # increment frequency in this document
                        self.index[word][key] += 1
                    else: # create new entry for this document
                        self.index[word] = {key: 1}

            print(self.index)

            title = page.find('title')
            heading_1 = page.find('h1')
            heading_2 = page.find('h2')
            heading_3 = page.find('h3')
            bold = page.find('b')
            if title:
                pass
            if heading_1:
                pass
            if heading_2:
                pass
            if heading_3:
                pass
            if bold:
                pass


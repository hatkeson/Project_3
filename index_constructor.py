from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import nltk.corpus
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
        self.index = {}     # only for inverted index
        self.title_index = {}
        self.heading_index = {}
        self.bold_index = {}

        self.stopwords = []
        with open('stopwords.txt') as file:
            for line in file:
                self.stopwords.append(line.rstrip())

    def read_corpus(self, corpus_path):
        nltk_words = set(nltk.corpus.words.words())
        # get the bookkeeping file
        with open(corpus_path + '\\bookkeeping.json') as f:
            bookkeeping = json.load(f)

        # for each entry in bookkeeping, navigate to the folder and then file, and read it with BS
        # first number is folder
        # second number is file
        for key in bookkeeping:
            folder_file = key.split('/')
            if folder_file[0] != '0':   # hardcoded limit, remove when ready for full corpus
                break
            with open(corpus_path + '\\' + folder_file[0] + '\\' + folder_file[1], 'rb') as f:
                page = BeautifulSoup(f, 'html.parser')

            tokenizer = WhitespaceTokenizer()
            lemmatizer = WordNetLemmatizer()

            # Handle titles, headings, and bold texts first
            title = page.find('title')
            heading_1 = page.find('h1')
            heading_2 = page.find('h2')
            heading_3 = page.find('h3')
            bold = page.find('b')
            if title and not title.string == "":
                try:
                    text_tokens = tokenizer.tokenize(title.string)
                    text_tokens = [w for w in text_tokens if w.lower() in nltk_words]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))
                    # add to inverted index
                    # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                    for word in text_tokens:
                        if word not in self.stopwords:
                            if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                                self.index[word][0][key] += 1
                            else:  # create new entry for this document
                                self.index[word] = [{key: 1}, 4, 0]  # List order: [{docID: freq}, type, tf-idf]
                except TypeError:
                    pass

            if heading_1 and not heading_1.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_1.string)
                    text_tokens = [w for w in text_tokens if w.lower() in nltk_words]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))
                    # add to inverted index
                    # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                    for word in text_tokens:
                        if word not in self.stopwords:
                            if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                                self.index[word][0][key] += 1
                            else:  # create new entry for this document
                                self.index[word] = [{key: 1}, 3, 0]  # List order: [{docID: freq}, type, tf-idf]
                except TypeError:
                    pass

            if heading_2 and not heading_2.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_2.string)
                    text_tokens = [w for w in text_tokens if w.lower() in nltk_words]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))
                    # add to inverted index
                    # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                    for word in text_tokens:
                        if word not in self.stopwords:
                            if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                                self.index[word][0][key] += 1
                            else:  # create new entry for this document
                                self.index[word] = [{key: 1}, 3, 0]  # List order: [{docID: freq}, type, tf-idf]
                except TypeError:
                    pass

            if heading_3 and not heading_3.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_3.string)
                    text_tokens = [w for w in text_tokens if w.lower() in nltk_words]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))
                    # add to inverted index
                    # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                    for word in text_tokens:
                        if word not in self.stopwords:
                            if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                                self.index[word][0][key] += 1
                            else:  # create new entry for this document
                                self.index[word] = [{key: 1}, 3, 0]  # List order: [{docID: freq}, type, tf-idf]
                except TypeError:
                    pass

            if bold and not bold.string == "":
                try:
                    text_tokens = tokenizer.tokenize(bold.string)
                    text_tokens = [w for w in text_tokens if w.lower() in nltk_words]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))
                    # add to inverted index
                    # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                    for word in text_tokens:
                        if word not in self.stopwords:
                            if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                                self.index[word][0][key] += 1
                            else:  # create new entry for this document
                                self.index[word] = [{key: 1}, 2, 0]  # List order: [{docID: freq}, type, tf-idf]
                except TypeError:
                    pass

            # tokenize
            # Whitespace tokenizer - keep contractions because they're in stopwords
            text_tokens = tokenizer.tokenize(page.get_text())
            # delete non-english words
            text_tokens = [w for w in text_tokens if w.lower() in nltk_words]

            # lemmatize - must strip leading and trailing punctuation because whitespace
            # tokenizer leaves them in
            text_tokens_len = len(text_tokens)
            for i in range(0, text_tokens_len):
                text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

            # add to inverted index
            # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
            for word in text_tokens:
                if word not in self.stopwords:
                    if word in self.index and key in self.index[word][0]:  # increment frequency in this document
                        self.index[word][0][key] += 1
                        pass
                    else:  # create new entry for this document
                        self.index[word] = [{key: 1}, 1, 0]  # List order: [{docID: freq}, type, tf-idf]

        print(self.index)
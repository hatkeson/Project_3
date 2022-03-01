from nltk import ngrams
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
import nltk.corpus
from string import punctuation
import json
from bs4 import BeautifulSoup
import numpy as np


# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)

class InvertedBigramIndex:
    def __init__(self):
        self.document_count = 0
        self.index = {}  # only for inverted index
        self.title = []
        self.heading = []
        self.bold = []
        self.bigrams = []
        self.stopwords = []

        with open('stopwords.txt') as file:
            for line in file:
                self.stopwords.append(line.rstrip())

    def read_corpus(self, corpus_path):
        # get the bookkeeping file
        with open(corpus_path + '\\bookkeeping.json') as f:
            bookkeeping = json.load(f)

        # for each entry in bookkeeping, navigate to the folder and then file, and read it with BS
        # first number is folder
        # second number is file
        for key in bookkeeping:
            folder_file = key.split('/')
            # if folder_file[0] != '0':   # hardcoded limit, remove when ready for full corpus
            #     break
            with open(corpus_path + '\\' + folder_file[0] + '\\' + folder_file[1], 'rb') as f:
                self.document_count += 1
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
                    text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

                    #get bigram from the text_tokens
                    self.bigrams = self.get_bigrams(text_tokens)

                    # filter out stopwords and modify self.bigram
                    self.filter_stopwords_in_bigrams()

                    # add to inverted bigram-index
                    for words in self.bigrams:
                        if words in self.index:  # we've seen this word before
                            if key in self.index[words]:  # in this document
                                self.index[words][key][0] += 1
                            else:  # seen word in other document
                                self.index[words][key] = [1, 4, 0]
                        else:  # haven't seen this word before
                            self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}
                except TypeError:
                    pass


                    # for word in text_tokens:
                    #     if word not in self.stopwords:
                    #         if word in self.index:  # we've seen this word before
                    #             if key in self.index[word]:  # in this document
                    #                 self.index[word][key][0] += 1
                    #             else:  # seen word in other document
                    #                 self.index[word][key] = [1, 4, 0]
                    #         else:  # haven't seen this word before
                    #             self.index[word] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}


            if heading_1 and not heading_1.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_1.string)
                    text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

                    # get bigram from the text_tokens
                    self.bigrams = self.get_bigrams(text_tokens)

                    # filter out stopwords and modify self.bigram
                    self.filter_stopwords_in_bigrams()

                    # add to inverted bigram-index
                    for words in self.bigrams:
                        if words in self.index:  # we've seen this word before
                            if key in self.index[words]:  # in this document
                                self.index[words][key][0] += 1
                            else:  # seen word in other document
                                self.index[words][key] = [1, 4, 0]
                        else:  # haven't seen this word before
                            self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}
                except TypeError:
                    pass
                #     # add to inverted index
                #     # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                #     for word in text_tokens:
                #         if word not in self.stopwords:
                #             if word in self.index:  # we've seen this word before
                #                 if key in self.index[word]:  # in this document
                #                     self.index[word][key][0] += 1
                #                 else:  # seen word in other document
                #                     self.index[word][key] = [1, 3, 0]
                #             else:  # haven't seen this word before
                #                 self.index[word] = {key: [1, 3, 0]}  # List order: {docID: [freq, type, tf-idf]}
                # except TypeError:
                #     pass

            if heading_2 and not heading_2.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_2.string)
                    text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

                    # get bigram from the text_tokens
                    self.bigrams = self.get_bigrams(text_tokens)

                    # filter out stopwords and modify self.bigram
                    self.filter_stopwords_in_bigrams()

                    # add to inverted bigram-index
                    for words in self.bigrams:
                        if words in self.index:  # we've seen this word before
                            if key in self.index[words]:  # in this document
                                self.index[words][key][0] += 1
                            else:  # seen word in other document
                                self.index[words][key] = [1, 4, 0]
                        else:  # haven't seen this word before
                            self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}
                except TypeError:
                    pass


                #     # add to inverted index
                #     # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                #     for word in text_tokens:
                #         if word not in self.stopwords:
                #             if word in self.index:  # we've seen this word before
                #                 if key in self.index[word]:  # in this document
                #                     self.index[word][key][0] += 1
                #                 else:  # seen word in other document
                #                     self.index[word][key] = [1, 3, 0]
                #             else:  # haven't seen this word before
                #                 self.index[word] = {key: [1, 3, 0]}  # List order: {docID: [freq, type, tf-idf]}
                # except TypeError:
                #     pass

            if heading_3 and not heading_3.string == "":
                try:
                    text_tokens = tokenizer.tokenize(heading_3.string)
                    text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))


                    # get bigram from the text_tokens
                    self.bigrams = self.get_bigrams(text_tokens)

                    # filter out stopwords and modify self.bigram
                    self.filter_stopwords_in_bigrams()

                    # add to inverted bigram-index
                    for words in self.bigrams:
                        if words in self.index:  # we've seen this word before
                            if key in self.index[words]:  # in this document
                                self.index[words][key][0] += 1
                            else:  # seen word in other document
                                self.index[words][key] = [1, 4, 0]
                        else:  # haven't seen this word before
                            self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}
                except TypeError:
                    pass

                #     # add to inverted index
                #     # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                #     for word in text_tokens:
                #         if word not in self.stopwords:
                #             if word in self.index:  # we've seen this word before
                #                 if key in self.index[word]:  # in this document
                #                     self.index[word][key][0] += 1
                #                 else:  # seen word in other document
                #                     self.index[word][key] = [1, 3, 0]
                #             else:  # haven't seen this word before
                #                 self.index[word] = {key: [1, 3, 0]}  # List order: {docID: [freq, type, tf-idf]}
                # except TypeError:
                #     pass

            if bold and not bold.string == "":
                try:
                    text_tokens = tokenizer.tokenize(bold.string)
                    text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]
                    text_tokens_len = len(text_tokens)
                    for i in range(0, text_tokens_len):
                        text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))


                    # get bigram from the text_tokens
                    self.bigrams = self.get_bigrams(text_tokens)

                    # filter out stopwords and modify self.bigram
                    self.filter_stopwords_in_bigrams()

                    # add to inverted bigram-index
                    for words in self.bigrams:
                        if words in self.index:  # we've seen this word before
                            if key in self.index[words]:  # in this document
                                self.index[words][key][0] += 1
                            else:  # seen word in other document
                                self.index[words][key] = [1, 4, 0]
                        else:  # haven't seen this word before
                            self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}
                except TypeError:
                    pass

                #     # add to inverted index
                #     # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
                #     for word in text_tokens:
                #         if word not in self.stopwords:
                #             if word in self.index:  # we've seen this word before
                #                 if key in self.index[word]:  # in this document
                #                     self.index[word][key][0] += 1
                #                 else:  # seen word in other document
                #                     self.index[word][key] = [1, 2, 0]
                #             else:  # haven't seen this word before
                #                 self.index[word] = {key: [1, 2, 0]}  # List order: {docID: [freq, type, tf-idf]}
                # except TypeError:
                #     pass

            # tokenize
            # Whitespace tokenizer - keep contractions because they're in stopwords
            text_tokens = tokenizer.tokenize(page.get_text())
            # delete non-english words
            text_tokens = [w for w in text_tokens if w.isalpha() and w.isascii()]

            # lemmatize - must strip leading and trailing punctuation because whitespace
            # tokenizer leaves them in
            text_tokens_len = len(text_tokens)
            for i in range(0, text_tokens_len):
                text_tokens[i] = lemmatizer.lemmatize(str.lower(text_tokens[i].strip(punctuation)))

                # get bigram from the text_tokens
                self.bigrams = self.get_bigrams(text_tokens)

                # filter out stopwords and modify self.bigram
                self.filter_stopwords_in_bigrams()

                # add to inverted bigram-index
                for words in self.bigrams:
                    if words in self.index:  # we've seen this word before
                        if key in self.index[words]:  # in this document
                            self.index[words][key][0] += 1
                        else:  # seen word in other document
                            self.index[words][key] = [1, 4, 0]
                    else:  # haven't seen this word before
                        self.index[words] = {key: [1, 4, 0]}  # List order: {docID: [freq, type, tf-idf]}



            # # add to inverted index
            # # TODO: UPDATE FREQUENCY PROPERLY (is this correct?)
            # for word in text_tokens:
            #     if word not in self.stopwords:
            #         if word in self.index:  # we've seen this word before
            #             if key in self.index[word]:  # in this document
            #                 self.index[word][key][0] += 1
            #             else:  # seen word in other document
            #                 self.index[word][key] = [1, 1, 0]
            #         else:  # haven't seen this word before
            #             self.index[word] = {key: [1, 1, 0]}  # List order: {docID: [freq, type, tf-idf]}

    def calculate_tf_idf(self):
        for word in self.index:
            for doc in self.index[word]:
                self.index[word][doc][2] = ((1 + np.log10(self.index[word][doc][0])) *
                                            (np.log10(self.document_count) / len(self.index[word])))

                # self.index[word][doc][0] # term frequency in this document
                # self.document_count # N
                # len(self.index[word]) # length of posting list
                # self.index[word][doc][2] # assign tf-idf
        # print(self.index)

    def write_to_json(self):
        # Write the index into a json file
        json_string = json.dumps(self.index)
        with open('bigram_index_text_file.json.json', 'w') as outFile:
            json.dump(json_string, outFile)

    def get_bigrams(self, tokens):
        bigrams = ngrams(tokens, 2)
        return [' '.join(grams) for grams in bigrams]
    
    def filter_stopwords_in_bigrams(self):
        if self.bigrams is not None:
            for words in self.bigrams:
                tokenizer = WhitespaceTokenizer()
                tokens = tokenizer.tokenize(words)
                #no need to lemmatize because the self.bigram should already have lemmatized words list

                for word in tokens:
                    if word in self.stopwords and not word == "":
                        self.bigrams.remove(word)

        return self.bigrams


# test = InvertedBigramIndex()
#
# test.read_corpus()

#reference from https://stackoverflow.com/questions/21844546/forming-bigrams-of-words-in-list-of-sentences-with-python
# text = ['cant railway station', 'citadel hotel', 'police stn']
# for line in text:
#     token = nltk.word_tokenize(line)
#     bigram = list(ngrams(token, 2))


# def get_bigrams(myString):
#     tokenizer = WordPunctTokenizer()
#     tokens = tokenizer.tokenize(myString)
#     stemmer = PorterStemmer()
#     bigram_finder = BigramCollocationFinder.from_words(tokens)
#     bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)
#
#     for bigram_tuple in bigrams:
#         x = "%s %s" % bigram_tuple
#         tokens.append(x)
#
#     result = [' '.join([stemmer.stem(w).lower() for w in x.split()]) for x in tokens if x.lower() not in stopwords.words('english') and len(x) > 8]
#     return result
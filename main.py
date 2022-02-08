import json
import sys
from bs4 import BeautifulSoup
import index_constructor

if __name__ == "__main__":

   # get directory of the webpages file
    webpages_folder = sys.argv[1]

    # get the bookkeeping file
    with open(webpages_folder + '\\bookkeeping.json') as f:
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
        with open(webpages_folder + '\\' + folder_file[0] + '\\' + folder_file[1], 'rb') as f:
            page = BeautifulSoup(f)
            title = page.find('title')
            heading = page.find('h1')
            bold = page.find('b')
        print(bold)

# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)

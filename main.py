import json
import sys
from bs4 import BeautifulSoup

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
        folder_file = key.split('/')
        print(bookkeeping[key])
        with open(webpages_folder + '\\' + folder_file[0] + '\\' + folder_file[1], 'rb') as f:
            page = BeautifulSoup(f)
        print(page)

# remove stop words
# lemmatize remaining tokens
# create inverted index
# store tf-idf
# note words in title, bold and heading (h1, h2, h3)

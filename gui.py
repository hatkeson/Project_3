from tkinter import *
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import webbrowser
import json
import ranking
import copy

def search_return_key(event):
    search()

def search():
    for item in results_list.get_children():
            results_list.delete(item)
    q = query_var.get().lower()
    if q:
        q_list = q.split()
        result_doc_list = list()

        # TODO: len(q_list) might return list of characters if query is single term? [DONE]
        # TODO: we prioritize bigram always? [DONE]
        # TODO: how does type work for 2+ queries?
        # TODO: how to even rank 2+ queries?
        # TODO: modify some parts to make more sense with ranking.py
        # TODO: KeyError crashes the GUI?

        # "hello there Mary hi" => [hello there, there Mary, Mary hi] => look up bigram for these 3 entries
        # cosine on the bigrams
        #

        if len(q_list) > 2:
            # rank bigram
            doc_list = ranking.ranked_results_by_unigrams(q, bindex_dict)
            result_doc_list.extend(doc_list)

            # TODO: modify this cuz ranked_results can handle single terms now
            # rank unigram if <20 bigram results
            if len(result_doc_list) < 20:
                doc_list = ranking.ranked_results_by_unigrams(q, index_dict)
                result_doc_list.extend(doc_list)

        # TODO: modify how we rank unigram after bigram is considered
        # Handle 2-term queries
        elif len(q_list) == 2:
            # tf-idf bigram
            # If the bigram exists
            if q in bindex_dict:
                doc_dict = copy.deepcopy(bindex_dict[q])
                doc_list = list(doc_dict)
                # modify tf-idf score based on type of text
                for doc in doc_list:
                    multiplier = 1
                    if doc_dict[doc][1] == 2:
                        multiplier = 1.5
                    elif doc_dict[doc][1] == 3:
                        multiplier = 2
                    elif doc_dict[doc][1] == 4:
                        multiplier = 2.5
                    doc_dict[doc][2] = doc_dict[doc][2] * multiplier

                sorted_docs = sorted(doc_dict.items(), key=lambda item: item[1][2], reverse=True)
                result_doc_list.extend(sorted_docs)

                # TODO: modify this cuz ranked_results can handle single terms now
                # rank unigram if < 20 bigram results
                if len(result_doc_list) < 20:
                    doc_list = ranking.ranked_results_by_unigrams(q, index_dict)
                    result_doc_list.extend(doc_list)
            # If the bigram doesnt exist, just check unigrams
            else:
                doc_list = ranking.ranked_results_by_unigrams(q, index_dict)
                result_doc_list.extend(doc_list)

        # TODO: modify this cuz ranked_results can handle single terms now
        else:
            # tf-idf with unigram
            if q in index_dict:
                doc_dict = copy.deepcopy(index_dict[q])
                doc_list = list(doc_dict)
                # modify tf-idf score based on type of text
                for doc in doc_list:
                    multiplier = 1
                    if doc_dict[doc][1] == 2:
                        multiplier = 1.5
                    elif doc_dict[doc][1] == 3:
                        multiplier = 2
                    elif doc_dict[doc][1] == 4:
                        multiplier = 2.5
                    doc_dict[doc][2] = doc_dict[doc][2] * multiplier

                sorted_docs = sorted(doc_dict.items(), key=lambda item: item[1][2], reverse=True)
                result_doc_list.extend(sorted_docs)


        result_count = 0
        for result in result_doc_list:
                if result[0] in bookkeeping and result_count < 20:
                    ######## NOTE: THIS IS PATH SPECIFIC ########
                    with open(r'D:\121 Project 3\webpages\WEBPAGES_RAW' + '\\' + result[0], 'rb') as f:
                        page = BeautifulSoup(f, 'html.parser')
                    try:
                        title = page.find('title').string.strip()
                        headings = ['h1','h2','h3','h4','h5','h6','strong']
                        i = 0
                        while not title:
                            title = page.find(headings[i]).string.strip()
                            i += 1
                    except AttributeError: # no valid title or heading
                            title = 'Untitled Document'
                    try:
                        desc = page.find('meta', attrs = {'name':'description'})['content']
                        if desc == "":
                            try:
                                desc = page.find('p').text.strip().splitlines()[0].strip()
                            except:
                                desc = 'Description Unavailable'
                    except TypeError: # no meta description
                        try:
                            desc = page.find('p').text.strip().splitlines()[0].strip()
                        except: # no text in the page
                            desc = 'Description Unavailable'
                    results_list.insert('', 'end', text = title, values=(desc, bookkeeping[result[0]]))
                result_count += 1
            #print(str(result_count) + ' results.')











        # if ' ' not in q:
        #     # rank single-term queries here
        #     doc_dict = copy.deepcopy(index_dict[q])
        #     doc_list = list(doc_dict)
        #     # modify tf-idf score based on type of text
        #     for doc in doc_list:
        #         multiplier = 1
        #         if doc_dict[doc][1] == 2:
        #             multiplier = 1.5
        #         elif doc_dict[doc][1] == 3:
        #             multiplier = 2
        #         elif doc_dict[doc][1] == 4:
        #             multiplier = 2.5
        #         doc_dict[doc][2] = doc_dict[doc][2] * multiplier
        #     #print(doc_dict)
        #     #print(index_dict[q])

        #     sorted_docs = sorted(doc_dict.items(), key=lambda item: item[1][2], reverse=True)

        #     result_count = 0
        #     for result in sorted_docs:
        #         if result[0] in bookkeeping and result_count < 20:
        #             with open(r'C:\Users\User\Documents\CS 121\Project_3\WEBPAGES_RAW' + '\\' + result[0], 'rb') as f:
        #                 page = BeautifulSoup(f, 'html.parser')
        #             try:
        #                 title = page.find('title').string.strip()
        #                 headings = ['h1','h2','h3','h4','h5','h6','strong']
        #                 i = 0
        #                 while not title:
        #                     title = page.find(headings[i]).string.strip()
        #                     i += 1
        #             except AttributeError: # no valid title or heading
        #                     title = 'Untitled Document'
        #             try:
        #                 desc = page.find('meta', attrs = {'name':'description'})['content']
        #             except TypeError: # no meta description
        #                 try:
        #                     desc = page.find('p').text.strip().splitlines()[0].strip()
        #                 except: # no text in the page
        #                     desc = 'Description Unavailable'
        #             results_list.insert('', 'end', text = title, values=(desc, bookkeeping[result[0]]))
        #         result_count += 1
        #     #print(str(result_count) + ' results.')

        # else:
        #     # check bigram index



        #     doc_dict = copy.deepcopy(bindex_dict[q])
        #     doc_list = list(doc_dict)
        #     # modify tf-idf score based on type of text
        #     for doc in doc_list:
        #         multiplier = 1
        #         if doc_dict[doc][1] == 2:
        #             multiplier = 1.5
        #         elif doc_dict[doc][1] == 3:
        #             multiplier = 2
        #         elif doc_dict[doc][1] == 4:
        #             multiplier = 2.5
        #         doc_dict[doc][2] = doc_dict[doc][2] * multiplier
        #     #print(doc_dict)
        #     #print(index_dict[q])

        #     sorted_docs = sorted(doc_dict.items(), key=lambda item: item[1][2], reverse=True)










        #     # get ranked result dict here
        #     doc_list = ranking.ranked_results(q, index_dict) # ranking of one-gram index
        #     result_count = 0
        #     for result in doc_list:
        #         if result[0] in bookkeeping and result_count < 20:
        #             with open(r'C:\Users\User\Documents\CS 121\Project_3\WEBPAGES_RAW' + '\\' + result[0], 'rb') as f:
        #                 page = BeautifulSoup(f, 'html.parser')
        #             try:
        #                 title = page.find('title').string.strip()
        #                 headings = ['h1','h2','h3','h4','h5','h6','strong']
        #                 i = 0
        #                 while not title:
        #                     title = page.find(headings[i]).string.strip()
        #                     i += 1
        #             except AttributeError: # no valid title or heading
        #                     title = 'Untitled Document'
        #             try:
        #                 desc = page.find('meta', attrs = {'name':'description'})['content']
        #             except TypeError: # no meta description
        #                 try:
        #                     desc = page.find('p').text.strip().splitlines()[0].strip()
        #                 except: # no text in the page
        #                     desc = 'Description Unavailable'
        #             results_list.insert('', 'end', text = title, values=(desc, bookkeeping[result[0]]))
        #             result_count += 1

def url_click(event):
    input_id = results_list.selection()
    input_item = results_list.item(input_id,)['values'][1]
    print(input_item)
    webbrowser.open('{}'.format(input_item))

with open('index_text_file.json') as file:
    index = json.load(file)
    index_dict = json.loads(index)

with open('bigram_index_text_file.json') as file:
    bindex_dict = json.load(file)

######## NOTE: THIS IS PATH SPECIFIC ########
with open('D:\\121 Project 3\webpages\WEBPAGES_RAW\\bookkeeping.json') as b:
    bookkeeping = json.load(b)

root = Tk() # creates window
root.title("Search Engine") # gives window a title

frm = ttk.Frame(root, padding=10) # creates frame inside window
frm.grid() # we want elements laid out in a grid (other option is "pack")

query_var = tk.StringVar() # this stores user input
entry = ttk.Entry(frm, width=50, textvariable=query_var) # text box where user enters query
entry.grid(column=0, row=0) # we'll place it in cell (0,0) in the grid
entry.bind("<Return>", search_return_key) # user triggers search function by pressing enter

search_button = ttk.Button(frm, text="Search", command=search) # command is pointer to function
search_button.grid(column=0, row=1) # put it in cell (0,1)

results_list = ttk.Treeview(frm, columns=['Description','URL'], height=20) # where results will be displayed
results_list.heading('#0', text='Title', anchor=tk.W)
results_list.column('#0', minwidth=0, width=300)
results_list.heading('Description', text='Description', anchor=tk.W)
results_list.column('Description', minwidth=0, width=300)
results_list.heading('URL', text='URL', anchor=tk.W)
results_list.column('URL', minwidth=0, width=300)
results_list.grid(column=0, row=2) # put it in cell (2,0)
results_list.bind("<Double-1>", url_click)

root.mainloop() # run the window
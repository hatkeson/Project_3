from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
import json
import ranking

def search_return_key(event):
    search()

def search():
    for item in results_list.get_children():
            results_list.delete(item)
    q = query_var.get()
    if q:
        if ' ' not in q:
            result_count = 0
            for result in index_dict[q]:
                if result in bookkeeping and result_count < 20:
                    print(bookkeeping[result])
                    results_list.insert('', 'end', text = '', values=(bookkeeping[result])) # replace text with Title
                    result_count += 1
            #print(str(result_count) + ' results.')
        else:
            # get ranked result dict here
            doc_list = ranking.ranked_results(q, index_dict)
            result_count = 0
            for result in doc_list:
                if result[0] in bookkeeping and result_count < 20:
                    print(bookkeeping[result[0]])
                    results_list.insert('', 'end', text='', values=(bookkeeping[result[0]]))  # replace text with Title
                    result_count += 1


with open('index_text_file.json') as file:
    index = json.load(file)
    index_dict = json.loads(index)

with open('D:\\121 Project 3\webpages\WEBPAGES_RAW\\bookkeeping.json') as b:
    bookkeeping = json.load(b)

root = Tk() # creates window
root.title("Search Engine") # gives window a title

frm = ttk.Frame(root, padding=10) # creates frame inside window
frm.grid() # we want elements laid out in a grid (other option is "pack")

query_var = tk.StringVar() # this stores user input
entry = ttk.Entry(frm, textvariable=query_var) # text box where user enters query
entry.grid(column=0, row=0) # we'll place it in cell (0,0) in the grid
entry.bind("<Return>", search_return_key) # user triggers search function by pressing enter

search_button = ttk.Button(frm, text="Search", command=search) # command is pointer to function
search_button.grid(column=1, row=0) # put it in cell (0,1)

results_list = ttk.Treeview(frm, columns=['URL'], height=20) # where results will be displayed
results_list.heading('#0', text='Title', anchor=tk.W)
results_list.heading('URL', text='URL', anchor=tk.W)
results_list.grid(column=0, row=2) # put it in cell (2,0)

root.mainloop() # run the window
from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
import json

def search_return_key(event):
    search()

def search():
    q = query_var.get()
    if q:
        print(q)


root = Tk()
root.title("Search Engine")

frm = ttk.Frame(root, padding=10)
frm.grid()

query_var = tk.StringVar()
entry = ttk.Entry(frm, textvariable=query_var)
entry.grid(column=0, row=0)
entry.bind("<Return>", search_return_key)

search_button = ttk.Button(frm, text="Search", command=search)
search_button.grid(column=1, row=0)

results_list = ttk.Treeview(frm)
results_list.grid(column=0, row=2)

root.mainloop()
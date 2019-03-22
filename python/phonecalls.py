import tkinter as tk
from tkinter import ttk
import webbrowser

from tkinter import messagebox as mbox
from tkinter import Menu


win = tk.Tk()
win.title("Emacs")
menuBar = Menu(win)
win.config(menu=menuBar)
therow = 0


def search():
    ie = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
    ie.open('https://mail.google.com/mail/u/0/#search/'+name.get())

filenameframe = ttk.LabelFrame(win,text='Filenames')
filenameframe.grid(column=0,row=therow,padx=8,pady=4)

therow = therow + 1
alabel = ttk.Label(win,text="Phone Number:")
alabel.grid(sticky=tk.W,row=therow,column=1)

# Adding a Textbox Entry widget
therow = therow + 1
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

therow = therow + 1
actiondeleteweekly  = ttk.Button(win,text = "Search", command=search)
actiondeleteweekly.grid(row=therow,sticky=tk.W,column=1)
win.mainloop()

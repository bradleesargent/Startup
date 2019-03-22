import Tkinter as tk
import ttk
win = tk.Tk()
win.title("Python Gui")
#win.resizable(0,0)
ttk.Label(win,text="A new label").grid(column=0,row=0)
win.mainloop()

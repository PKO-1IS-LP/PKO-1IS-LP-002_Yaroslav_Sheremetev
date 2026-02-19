from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My gui app")
root.geometry("250x200")

ttk.Entry().pack(anchor=NW, padx=8, pady=8)

root.mainloop()
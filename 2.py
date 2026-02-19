from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My First GUI app!")
root.iconbitmap(default="tree.ico")
root.geometry("300x250")

label = Label(text="Hello world")
label.pack()
root.mainloop()
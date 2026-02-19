from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My gui app")
root.geometry("250x200")

btn = ttk.Button(text="Click Me", state=["disabled"])
btn.pack()

root.mainloop()
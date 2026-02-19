from tkinter import *
from datetime import datetime as dt

def insert_time():
    t = dt.now().time()
    e1.insert(0, t.strftime('%H:%M:%S '))

root = Tk()
root.title("Вставка времени")
root.geometry("300x100")

e1 = Entry(width=50)
but = Button(text="время", command=insert_time)
e1.pack(pady=10)
but.pack()

root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()

f_top = LabelFrame(text="Верх")  # Исправлено "Bepx" на "Верх"
f_bot = LabelFrame(text="Низ")   # Исправлено "Hus" на "Низ"

l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text="3")
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text="4")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4.pack(side=LEFT)

f_top.pack()
f_bot.pack()

root.mainloop()
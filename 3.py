from tkinter import *
from tkinter import ttk    # подключаем пакет ttk

root = Tk()
root.title("my gui app")
root.geometry("250x200")

btn = ttk.Button(text="click")  # создаем кнопку из пакета ttk
btn.pack()    # размещаем кнопку в окне

root.mainloop()
from tkinter import *
root = Tk()

l1 = Label(text="машинное обучение", font="Arial 32")
l2 = Label(text="Распознавание образов",
    font=("Comic Sans MS", 24, "bold"))

l1.config(bg='#ffaaaa')
l2.config(bg='#aaffff')

l1.pack()
l2.pack()

root.mainloop()
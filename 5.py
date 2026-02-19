from tkinter import *
from tkinter import ttk

root = Tk()
root.title("my gui app")
root.geometry("250x150")

btn = ttk.Button()
btn.pack()

# устанавливаем параметр text
btn["text"] = "send"
# получаем значение параметра text
btnText = btn["text"]
print(btnText)

# устанавливаем параметр text
btn.config(text="Send Email")
btnText = btn["text"]
print(btnText)

root.mainloop()
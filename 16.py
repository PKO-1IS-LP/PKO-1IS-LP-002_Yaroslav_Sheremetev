from tkinter import *
from tkinter import ttk
import re

def is_valid(newval):
    result = re.match("^\\+{0,1}\d{0,11}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set("Номер телефона должен быть в формате +XXXXXXXXXXX, где x представляет цифру")
    else:
        errmsg.set("")
    return result

root = Tk()
root.title("My gui app")
root.geometry("250x200")

check = (root.register(is_valid), "%P")

errmsg = StringVar()

phone_entry = ttk.Entry(validate="key", validatecommand=check)
phone_entry.pack(pady=5, padx=5, anchor=NW)

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(pady=5, padx=5, anchor=NW)

root.mainloop()
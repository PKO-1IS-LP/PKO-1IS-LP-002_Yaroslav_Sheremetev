from tkinter import *
from tkinter import ttk

def show_position(pos):
    descriptions = {
        "NW": "верхний левый угол",
        "N": "вверху по центру",
        "NE": "верхний правый угол",
        "W": "слева по центру",
        "CENTER": "центр",
        "E": "справа по центру",
        "SW": "нижний левый угол",
        "S": "внизу по центру",
        "SE": "нижний правый угол"
    }
    label.config(text=f"Кнопка {pos}: {descriptions[pos]}")

root = Tk()
root.title("Кнопки по диагонали")
root.geometry("300x300")

# Метка для вывода сообщения
label = Label(root, text="Нажмите на кнопку", font=("Arial", 12))
label.grid(row=3, column=0, columnspan=3, pady=10)

# Сетка 3x3 с кнопками
buttons = [
    ["NW", "N", "NE"],
    ["W", "CENTER", "E"],
    ["SW", "S", "SE"]
]

for i in range(3):
    for j in range(3):
        pos = buttons[i][j]
        btn = Button(root, text=pos, width=10, height=3,
                     command=lambda p=pos: show_position(p))
        btn.grid(row=i, column=j, padx=2, pady=2)

root.mainloop()
from tkinter import *
from tkinter import ttk

def show_color(color_code, color_name):
    # Вставляем код цвета
    entry.delete(0, END)
    entry.insert(0, color_code)
    # Обновляем метку с названием цвета
    label.config(text=color_name)


root = Tk()
root.title("Цвета радуги")
root.geometry("300x250")

# Создаем текстовое поле для отображения кода цвета
entry = Entry(width=20, justify=CENTER, font=("Arial", 12))
entry.pack(pady=10)

# Создаем метку для отображения названия цвета
label = Label(font=("Arial", 14), width=20)
label.pack(pady=5)

# Создаем рамку для кнопок
button_frame = Frame()
button_frame.pack(pady=10)

# Словарь с цветами радуги (код цвета: название)
colors = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый"
}

# Создаем кнопки для каждого цвета
row = 0
col = 0
for color_code, color_name in colors.items():
    btn = Button(
        button_frame,
        bg=color_code,
        width=5,
        height=2,
        command=lambda code=color_code, name=color_name: show_color(code, name)
    )
    btn.grid(row=row, column=col, padx=2, pady=2)

    col += 1
    if col > 2:  # После 3 кнопок переходим на новую строку
        col = 0
        row += 1

root.mainloop()
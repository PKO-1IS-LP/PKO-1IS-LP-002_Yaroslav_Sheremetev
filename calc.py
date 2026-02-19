from tkinter import *
from tkinter import ttk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result_label.config(text="ошибка")
                return
            result = num1 / num2

        # Округляем результат до 2 знаков, если это не целое число
        if result.is_integer():
            result_label.config(text=str(int(result)))
        else:
            result_label.config(text=str(round(result, 2)))

    except ValueError:
        result_label.config(text="ошибка")


root = Tk()
root.title("Калькулятор")
root.geometry("250x200")

# Поля для ввода чисел
entry1 = Entry(width=15)
entry1.pack(pady=5)

entry2 = Entry(width=15)
entry2.pack(pady=5)

# Рамка для кнопок
button_frame = Frame()
button_frame.pack(pady=10)

# Кнопки операций
btn_plus = Button(button_frame, text="+", width=5, command=lambda: calculate('+'))
btn_plus.grid(row=0, column=0, padx=2)

btn_minus = Button(button_frame, text="-", width=5, command=lambda: calculate('-'))
btn_minus.grid(row=0, column=1, padx=2)

btn_mult = Button(button_frame, text="*", width=5, command=lambda: calculate('*'))
btn_mult.grid(row=1, column=0, padx=2, pady=2)

btn_div = Button(button_frame, text="/", width=5, command=lambda: calculate('/'))
btn_div.grid(row=1, column=1, padx=2, pady=2)

# Метка для результата
result_label = Label(text="0", font=("Arial", 14), width=15, bg='lightgray', fg='black')
result_label.pack(pady=10)

root.mainloop()
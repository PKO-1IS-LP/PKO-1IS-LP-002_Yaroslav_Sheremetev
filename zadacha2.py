from tkinter import *  # импортируем все классы и функции из библиотеки tkinter

# Функция для обработки нажатия кнопки Submit
def submit_action():
    # меняем текст метки на "Выполнен вход"
    result_label.config(text="Выполнен вход")

# Функция для очистки полей ввода
def clear_action():
    username_entry.delete(0, END)  # удаляем текст из поля username от начала до конца
    password_entry.delete(0, END)  # удаляем текст из поля password от начала до конца

# Функция для закрытия приложения
def close_action():
    root.destroy()  # закрываем главное окно и завершаем программу

# Создаём главное окно
root = Tk()
root.title("Форма авторизации")  # заголовок окна
root.geometry("300x200")          # устанавливаем размер окна (ширина 300, высота 200)
root.resizable(False, False)      # запрещаем изменение размеров окна

# Создаём метку для поля Username
Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
# Поле ввода для имени пользователя
username_entry = Entry(root, width=20)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Метка для поля Password
Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
# Поле ввода для пароля (символы скрываются звёздочками)
password_entry = Entry(root, width=20, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Кнопка Submit с привязкой функции submit_action
submit_btn = Button(root, text="Submit", command=submit_action)
submit_btn.grid(row=2, column=0, padx=5, pady=5)

# Кнопка Clear с привязкой функции clear_action
clear_btn = Button(root, text="Clear", command=clear_action)
clear_btn.grid(row=2, column=1, padx=5, pady=5)

# Кнопка Close с привязкой функции close_action
close_btn = Button(root, text="Close", command=close_action)
close_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Метка для вывода результата (изначально пустая)
result_label = Label(root, text="", font=("Arial", 10))
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
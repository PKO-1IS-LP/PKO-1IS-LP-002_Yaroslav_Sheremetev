from tkinter import *
from tkinter import ttk

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "admin":
        result_label.config(text="Авторизация успешна!", fg="green")
    else:
        result_label.config(text="Неверный логин или пароль", fg="red")


root = Tk()
root.title("Авторизация")
root.geometry("300x200")
root.resizable(False, False)

# Заголовок
title_label = Label(root, text="Вход в систему", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Подписи и поля ввода
Label(root, text="Логин:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_username = Entry(root, width=20)
entry_username.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Пароль:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_password = Entry(root, width=20, show="*")
entry_password.grid(row=2, column=1, padx=5, pady=5)

# Кнопка входа
btn_login = Button(root, text="Войти", command=check_credentials)
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

# Метка для вывода результата
result_label = Label(root, text="", font=("Arial", 10))
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
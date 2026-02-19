import csv          # импорт модуля для работы с CSV-файлами
import os           # импорт модуля для работы с операционной системой (проверка существования файла)
from tkinter import *   # импорт всех классов и функций из библиотеки tkinter

def compute_hash(password):          # функция вычисления хеша пароля
    return sum(ord(ch) for ch in password)   # возвращает сумму кодов Unicode всех символов пароля

def hash_action():                   # функция, вызываемая при нажатии кнопки "Hash"
    pwd = entry.get()                 # получить текст из поля ввода
    if pwd:                           # если пароль не пустой
        h = compute_hash(pwd)          # вычислить хеш
        hash_label.config(text=f"Хеш: {h}")   # вывести хеш в метку
    else:                              # если пароль пустой
        hash_label.config(text="Введите пароль")   # вывести сообщение о необходимости ввода

def save_action():                    # функция сохранения в CSV при нажатии кнопки "Сохранить"
    pwd = entry.get()                  # получить пароль из поля ввода
    if not pwd:                        # если пароль пустой
        status_label.config(text="Введите пароль", fg="red")   # показать ошибку красным цветом
        return                          # выйти из функции
    h = compute_hash(pwd)               # вычислить хеш
    file_exists = os.path.isfile('passwords.csv')   # проверить, существует ли файл passwords.csv
    with open('passwords.csv', 'a', newline='', encoding='utf-8') as f:  # открыть файл для добавления (режим 'a')
        writer = csv.writer(f)          # создать объект для записи CSV
        if not file_exists:              # если файл только что создан (не существовал)
            writer.writerow(['Пароль', 'Хеш'])   # записать заголовки столбцов
        writer.writerow([pwd, h])        # записать строку с паролем и его хешем
    status_label.config(text="Сохранено", fg="green")   # вывести сообщение об успехе зелёным цветом

def clear_action():                    # функция очистки CSV-файла
    with open('passwords.csv', 'w', newline='', encoding='utf-8') as f:  # открыть файл для записи (перезапись)
        writer = csv.writer(f)          # создать объект для записи
        writer.writerow(['Пароль', 'Хеш'])   # записать только заголовки (очистить данные)
    status_label.config(text="Таблица очищена", fg="blue")   # вывести сообщение синим цветом

root = Tk()                            # создать главное окно приложения
root.title("Хеширование паролей")       # установить заголовок окна
root.geometry("350x250")                # установить размер окна (ширина 350, высота 250)
root.resizable(False, False)            # запретить изменение размеров окна

Label(root, text="Введите пароль:").grid(row=0, column=0, padx=5, pady=5, sticky='e')   # метка "Введите пароль:" размещена в сетке
entry = Entry(root, width=30, show="*")  # поле ввода пароля (ширина 30, символы скрыты звёздочкой)
entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)   # разместить поле в сетке, занимая 2 столбца

btn_hash = Button(root, text="Hash", command=hash_action)   # кнопка "Hash" с привязкой функции hash_action
btn_hash.grid(row=1, column=0, padx=5, pady=5)              # разместить кнопку в сетке

hash_label = Label(root, text="Хеш: не вычислен", font=("Arial", 10))   # метка для вывода хеша
hash_label.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky='w')   # разместить метку в сетке

btn_save = Button(root, text="Сохранить", command=save_action)   # кнопка "Сохранить" с привязкой save_action
btn_save.grid(row=2, column=0, padx=5, pady=5)                   # разместить кнопку

btn_clear = Button(root, text="Очистить", command=clear_action)   # кнопка "Очистить" с привязкой clear_action
btn_clear.grid(row=2, column=1, padx=5, pady=5)                   # разместить кнопку

status_label = Label(root, text="", font=("Arial", 9))            # метка для вывода статуса (изначально пустая)
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)  # разместить метку, занимающую три столбца

root.mainloop()                           # запустить главный цикл обработки событий окна
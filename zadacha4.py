from tkinter import *  # импортируем все классы и функции tkinter

def save_data():
    """
    Функция для сохранения данных из полей ввода в текстовый файл.
    Открывает файл students.txt в режиме добавления и записывает туда строку
    с именем, фамилией, классом и группой.
    """
    # Получаем данные из полей ввода
    name = name_entry.get().strip()          # имя, удаляем лишние пробелы
    surname = surname_entry.get().strip()    # фамилия
    grade = grade_entry.get().strip()        # класс
    group = group_entry.get().strip()        # группа

    # Проверяем, что все поля заполнены
    if name and surname and grade and group:
        # Открываем файл students.txt в режиме добавления (a) с кодировкой UTF-8
        with open("students.txt", "a", encoding="utf-8") as file:
            # Записываем строку с данными, разделёнными табуляцией, и переходим на новую строку
            file.write(f"{name}\t{surname}\t{grade}\t{group}\n")
        # Обновляем метку статуса, сообщаем об успехе
        status_label.config(text="Данные сохранены!", fg="green")
    else:
        # Если не все поля заполнены, выводим предупреждение
        status_label.config(text="Заполните все поля!", fg="red")

def clear_fields():
    """
    Функция очистки всех полей ввода.
    """
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    grade_entry.delete(0, END)
    group_entry.delete(0, END)
    status_label.config(text="")  # очищаем метку статуса

# Создаём главное окно
root = Tk()
root.title("Запись данных ученика")  # заголовок окна
root.geometry("350x250")              # размер окна (ширина 350, высота 250)
root.resizable(False, False)          # запрещаем изменение размеров окна

# Создаём метки и поля ввода с помощью grid-размещения

# Имя
Label(root, text="Имя:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Фамилия
Label(root, text="Фамилия:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
surname_entry = Entry(root, width=25)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

# Класс
Label(root, text="Класс:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
grade_entry = Entry(root, width=25)
grade_entry.grid(row=2, column=1, padx=5, pady=5)

# Группа
Label(root, text="Группа:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
group_entry = Entry(root, width=25)
group_entry.grid(row=3, column=1, padx=5, pady=5)

# Кнопка "Сохранить" – при нажатии вызывает save_data
save_btn = Button(root, text="Сохранить", command=save_data)
save_btn.grid(row=4, column=0, padx=5, pady=10)

# Кнопка "Очистить" – при нажатии вызывает clear_fields
clear_btn = Button(root, text="Очистить", command=clear_fields)
clear_btn.grid(row=4, column=1, padx=5, pady=10)

# Метка для отображения статуса (успех/ошибка)
status_label = Label(root, text="", font=("Arial", 10))
status_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Запускаем главный цикл обработки событий
root.mainloop()
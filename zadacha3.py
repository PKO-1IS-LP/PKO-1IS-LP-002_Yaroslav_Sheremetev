from tkinter import *  # импортируем все классы и функции tkinter

def analyze_data():
    """
    Функция для анализа данных из поля ввода.
    Разбивает строку по запятым, проверяет каждый элемент на наличие цифр.
    Выводит результат в метку.
    """
    input_text = entry.get()  # получаем текст из поля ввода
    if not input_text.strip():  # если строка пустая или состоит только из пробелов
        result_label.config(text="Введите данные")  # просим ввести данные
        return

    # Разбиваем по запятой, удаляем лишние пробелы у каждого элемента
    elements = [elem.strip() for elem in input_text.split(',') if elem.strip()]

    # Список элементов, содержащих хотя бы одну цифру
    elements_with_digits = []
    for elem in elements:
        if any(ch.isdigit() for ch in elem):  # если есть цифра
            elements_with_digits.append(elem)

    count = len(elements_with_digits)  # количество таких элементов

    if count > 0:
        # Формируем сообщение: есть цифры, и показываем количество и сами элементы
        result_text = f"Найдено элементов с цифрами: {count}\n"
        result_text += ", ".join(elements_with_digits)
        result_label.config(text=result_text)
    else:
        result_label.config(text="Цифры не найдены")

# Создаём главное окно
root = Tk()
root.title("Поиск цифр в данных")      # заголовок окна
root.geometry("400x250")                # размер окна
root.resizable(False, False)            # запрещаем изменение размеров

# Создаём метку-инструкцию
instruction = Label(root, text="Введите элементы через запятую:")
instruction.pack(pady=5)

# Поле ввода
entry = Entry(root, width=50)
entry.pack(pady=5)

# Кнопка для запуска анализа
analyze_btn = Button(root, text="Проверить", command=analyze_data)
analyze_btn.pack(pady=5)

# Метка для вывода результата
result_label = Label(root, text="", font=("Arial", 10), justify=LEFT, wraplength=380)
result_label.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()
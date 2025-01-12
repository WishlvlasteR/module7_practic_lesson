def custom_write(file_name, strings):
    """
    Ф-я записывает строки из списка в файл и возвращает словарь, где ключ - это № строки и № байта с которого
    начинается новая строка, а значение сама строка из списка записанная в файл.
    """
    strings_positions = {}  # Словарь для хранения позиций строк
    # Открываем файл для записи в режиме записи текста с кодировкой utf-8
    file = open('file_name.txt', 'w', encoding='utf-8')
    line_number = 1  # Переменная для хранения номера строки
    for string in strings:
        byte_position = file.tell()  # Получаем текущую позицию в байтах перед записью
        file.write(string + '\n')  # Записываем строку в файл с добавлением '\n' в конце
        strings_positions[(line_number, byte_position)] = string  # Добавляем данные в словарь
        line_number += 1  # Увеличиваем номер строки
    file.close()  # Закрываем файл
    return strings_positions  # Возвращаем словарь


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', info)
for elem in result.items():
    print(elem)

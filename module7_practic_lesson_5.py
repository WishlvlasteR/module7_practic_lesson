import os
import time


directory = r'D:\ProgramFiles\PythonProect\module7_practic_lesson'

# Обход каталога с использованием os.walk
for root, dirs, files in os.walk(directory):
  for file in files:
      # Формирование полного пути к файлу
    filepath = os.path.join(root, file)
      # Получение времени последнего изменения файла
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
      # Получение размера файла
    filesize = os.path.getsize(filepath)
      # Получение родительской директории файла
    parent_dir = os.path.dirname(filepath)
      # Вывод информации о файле
    print(f'\nОбнаружен файл: {file}\n Путь: {filepath}\n'
          f' Размер: {filesize} байт\n Время изменения: {formatted_time}\n'
          f' Родительская директория: {parent_dir}')
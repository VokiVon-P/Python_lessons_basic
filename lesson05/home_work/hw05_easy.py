__author__ = 'Павел Новиков (aka Paul VokiVon)'

import os
import shutil

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def dir_in_cwd():
    # print("---------- Задача 2 ----------")
    dirs = [ i for i in os.listdir(path=os.getcwd()) if os.path.isdir(i)]
    print(dirs)
    print()


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создаем новую директорию
def make_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Создана директория {dir_path}")
    except FileExistsError:
        print(f"Ошибка создания : Директория {dir_path} уже существует")


# Удаление директории
def del_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f"Удалена директория {dir_path}")
    except FileNotFoundError:
        print(f"Ошибка удаления : Директории {dir_path} не существует")

# Перейти в директорию
# для дз уровня нормал
def ch_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f"Перешли в директорию {dir_path}")
    except FileNotFoundError:
        print(f"Ошибка перехода : Директории {dir_path} не существует")


if __name__ == '__main__':
    # выполняетя только если основной модуль выполнения
    # при импорте не выполняется
    for i in range(10):
        make_dir(f'NewDir_{i}')
    dir_in_cwd()
    input("Нажмите Enter для удаления созданных директорий")
    for i in range(10):
        del_dir(f'NewDir_{i}')
    print()
    dir_in_cwd()

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    print("---------- Задача 3 ----------")
    print()
    print(f"Корируем файл {__file__}")
    shutil.copyfile(__file__, f"{__file__}_copy")
    print(os.listdir(os.getcwd()))
__author__ = 'Павел Новиков (aka Paul VokiVon)'

import os
# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
print("---------- Задача 2 ----------")

d_w = dict()
h_w = dict()

path = os.path.join('data', 'workers')
with open(path, 'r', encoding='UTF-8') as src_f:
    w_list = src_f.readlines()
    # print(w_list)
for i in w_list:
    if not w_list.index(i):
        continue
    x = i.split()
    d_w[f'{x[0]} {x[1]}'] = [int(x[2]), int(x[4])]
# print(d_w)


path = os.path.join('data', 'hours_of')
with open(path, 'r', encoding='UTF-8') as src_f:
    h_list = src_f.readlines()
    # print(h_list)
for i in h_list:
    if not h_list.index(i):
        continue
    x = i.split()
    h_w[f'{x[0]} {x[1]}'] = int(x[2])
# print(h_w)

for person in d_w:
    name = str(person)
    itm = d_w[person]
    salary = itm[0]
    hours = itm[1]
    hsal = round(salary/hours, 2)
    realhours = h_w[person]
    delta = realhours - hours
    total = round(realhours * hsal, 1)
    bonus = round(delta * hsal, 1)
    if delta > 0:
        bonus *=2
    print(f"{name} за отработку {realhours} вместо {hours} часов, получит {total} - из них бонус = {bonus}")
print()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("---------- Задача 3 ----------")
path = os.path.join('data', 'fruits.txt')
with open(path, 'r', encoding='UTF-8') as src_f:
    src = src_f.readlines()
    print(src)


def save_fruis_file(filename, fruits_list):
    # записываем в файл подготовленный список
    path_w = os.path.join('data', filename + '.txt')
    my_file = open(path_w, 'w', encoding='UTF-8')
    for i in fruits_list:
        my_file.write(i)
    my_file.close()


up_char_list = list(map(chr, range(ord('А'), ord('Я')+1)))
print(up_char_list)

for i in up_char_list:
    w_list = []
    for k in src:
        if k.startswith(i):
            w_list.append(k)
    if len(w_list):
        fname = str(i) + '_fruits'
        save_fruis_file(fname, w_list)
        print(fname)
        print(w_list)
        print()

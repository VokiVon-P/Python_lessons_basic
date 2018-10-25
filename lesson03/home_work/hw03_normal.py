__author__ = 'Павел Новиков (aka Paul VokiVon)'
import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("---------- Задача 1 ----------")
def fibonacci(n, m):

    # воспользуемся формулой Бине для расчета n-элемента ряда Фибоначчи и выделим в отдельную функцию
    def bine(k):
        if not k or k == 1:
            return 1
        else:
            index = math.sqrt(5)
            left = (1 + index) / 2
            right = (1 - index) / 2
            return int((math.pow(left, k) - math.pow(right, k))/index)

    # основное тело нашей функции
    if n < 1 or n > 48 or m < 1 or m > 48 or n > m:
        print("Аргументы могут быть в пределах от 1 до 48 !!!")
        return None
    i = int(n)
    arr_fibo = list()
    while i <= int(m):
        arr_fibo.append(bine(i))
        i += 1
    return arr_fibo


print(fibonacci(1, 12))
print()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("---------- Задача 2 ----------")

def sort_to_max(origin_list):
    #  пузырьком это уж совсем сурово - возьмем алгоритм чуть получше - выбором мах
    a = origin_list
    j = len(a) - 1
    while j > 0:
        m = 0
        for i in range(1, j + 1):
            if a[i] > a[m]:
                # запоминаем индекс максимума, для дальнейшей замены с последним элементом в range
                m = i
        a[m], a[j] = a[j], a[m]
        j -= 1
    return a  # для удобства возвращаем ссылку на начальный массив ( уже отсортированный )


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print()

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("---------- Задача 3 ----------")
arr = [1, 3, 0, 6, 17, 23, 48, 50]


def my_filter(func, itt):
    new_list = list()
    if func is not None:
        for i in itt:
            if func(i):
                new_list.append(i)
    return new_list


narr = my_filter(lambda x: x > 5, arr)
print(narr)
print()

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print("---------- Задача 4 ----------")
# Параллелограммом является такой четырехугольник,
# у которого диагонали разделены точкой пересечения пополам
# arr_A = [[10, 10], [15, 12], [20, 22], [15, 20]]
arr_A = []
for i in range(4):
    x, y = map(int, input(f"Введите координаты точки А{i+1} = x,y :").strip().split(","))
    arr_A.append([x, y])
print(arr_A)


def half_diag(point1, point3):
    x1, y1 = point1
    x3, y3 = point3
    xs = round(abs(x1+x3)/2, 3)
    ys = round(abs(y1+y3)/2, 3)
    return [xs, ys]


hd1 = half_diag(arr_A[0], arr_A[2])
hd2 = half_diag(arr_A[1], arr_A[3])
if hd1 == hd2:
    print("Являются вершинами параллелограмма")
else:
    print("Увы. Не являются вершинами параллелограмма")

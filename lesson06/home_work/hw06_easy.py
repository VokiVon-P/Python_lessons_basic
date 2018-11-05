__author__ = 'Павел Новиков (aka Paul VokiVon)'

import math

"""
Введем вспомогательный класс Point который послужит нам в дальшейших упражнениях
"""

class Point:
    """
    Класс для Точки - мне так проще работать с координатами
    """

    def __init__(self, x, y):
        # Координаты храним в атрибуте __coord (ну захотелось нам так)
        # Два символа подчеркивания __ разрешают доступ к атрибуту только внутри класса
        self.__x = x
        self.__y = y

    @property  # с помощью этого декоратора можем обращаться к атрибуту x --> self.x Или obj.x
    def x(self):
        return self.__x

    @x.setter  # Позволяет в удобной форме устанавливать атрибут x --> self.x = 10 или obj.x = 10
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def as_point(self):
        return [self.__x, self.__y]

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:
    """
    Класс для Треугольника - мне так проще работать с координатами
    """
    def __init__(self, point1, point2, point3):
        self.__pA = point1
        self.__pB = point2
        self.__pC = point3

    # хелпер - длинна отрезака по двум точкам
    def __lenside(self, point1, point2):
        dX = point1.x - point2.x
        dY = point1.y - point2.y
        qx = dX ** 2
        qy = dY ** 2
        l = math.sqrt(qx + qy)
        return l

    # хелпер - полупериметр
    def __p(self):
        p = (self.sideAB + self.sideBC + self.sideAC)/2
        return p

    @property
    def pointA(self):
        return self.__pA

    @property
    def pointB(self):
        return self.__pB

    @property
    def pointC(self):
        return self.__pC

    @property
    def altitude(self):
        return (self.area*2)/self.sideAC

    @property
    def area(self):
        return math.sqrt(self.__p() * (self.__p() - self.sideAB) * (self.__p() - self.sideBC) * (self.__p() - self.sideAC))

    @property
    def sideAB(self):
        return self.__lenside(self.pointA, self.pointB)

    @property
    def sideBC(self):
        return self.__lenside(self.pointB, self.pointC)

    @property
    def sideAC(self):
        return self.__lenside(self.pointA, self.pointC)

    @property
    def perimeter(self):
        return self.sideAC + self.sideAB + self.sideBC

    def as_3points(self):
        return [self.pointA, self.pointB, self.pointC]

    def __str__(self):
        return f'A({self.pointA}) B({self.pointB}) C({self.pointC})'



p1 = Point(0, 0)
p2 = Point(50, 50)
p3 = Point(100, 0)

trg = Triangle(p1, p2, p3)
print(f"Треугольник = {trg}")
print(f"периметр = {trg.perimeter}")
print(f"прощадь = {trg.area}")
print(f"высота = {trg.altitude}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


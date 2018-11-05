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

    # статическая функция расчета длинны отрезка между 2 точками
    def len_segment(point1, point2):
        dX = point1.x - point2.x
        dY = point1.y - point2.y
        qx = dX ** 2
        qy = dY ** 2
        l = math.sqrt(qx + qy)
        return l

    # расчет отрезка между данной точкой и переданной в аргументе
    def p_segment(self, point2):
        return Point.len_segment(self, point2)

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
        return Point.len_segment(point1, point2)
        # dX = point1.x - point2.x
        # dY = point1.y - point2.y
        # qx = dX ** 2
        # qy = dY ** 2
        # l = math.sqrt(qx + qy)
        # return l

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
        return round(self.sideAC + self.sideAB + self.sideBC, 3)

    def __str__(self):
        return f'Triangle: A({self.pointA}) B({self.pointB}) C({self.pointC})'



p1 = Point(0, 0)
p2 = Point(50, 50)
p3 = Point(100, 0)

trg = Triangle(p1, p2, p3)
print(f"Треугольник = {trg}")
print(f"периметр = {trg.perimeter}")
print(f"прощадь = {trg.area}")
print(f"высота = {trg.altitude}")
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezium:
    """
    Класс для Трапеции - в данном слечае ранобедеренной
    """
    def __init__(self,  point1, point2, point3, point4):
        self.__pA = point1
        self.__pB = point2
        self.__pC = point3
        self.__pD = point4

    def __init__(self, point_list):
        self.__pA = point_list[0]
        self.__pB = point_list[1]
        self.__pC = point_list[2]
        self.__pD = point_list[3]

    @property
    def side_a(self):
        return self.__pA.p_segment(self.__pB)

    @property
    def side_b(self):
        return self.__pB.p_segment(self.__pC)

    @property
    def side_c(self):
        return self.__pC.p_segment(self.__pD)

    @property
    def side_d(self):
        return self.__pD.p_segment(self.__pA)

    @property
    def is_equiside(self):
        # равнобедренность = равенство диагоналей
        d1 = self.__pA.p_segment(self.__pC)
        d2 = self.__pB.p_segment(self.__pD)
        return d1 == d2

    @property
    def perimeter(self):
        return round(self.side_a + self.side_b + self.side_c + self.side_d, 3)

    @property
    def area(self):
        k5 = self.side_d - self.side_b
        k1 = (self.side_b + self.side_d) / 2
        k2 = (k5)**2
        k3 = self.side_a**2
        k4 = self.side_c**2
        m1 = (k2 + k3 - k4) / (2 * k5)
        l2 = k3 - m1**2
        s1 = k1 * math.sqrt(l2)
        return s1

    def __str__(self):
        return f'Trapezium: A({self.__pA}) B({self.__pB}) C({self.__pC} D({self.__pD})'

# представим таким образом трапецию
p_list = [Point(0, 0), Point(50, 50), Point(100, 50), Point(150, 0)]
tpm = Trapezium(p_list)
print(f"Трапеция: {tpm}")
str1 = "Да" if tpm.is_equiside else "Нет"
print(f"Равнобедренная : {str1}")
print(f"Периметр : {tpm.perimeter}")
print(f"Площадь : {tpm.area}")


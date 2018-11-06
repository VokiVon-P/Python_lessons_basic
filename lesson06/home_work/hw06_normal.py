__author__ = 'Павел Новиков (aka Paul VokiVon)'

import random
import datetime

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

# Общую информацию выносим в Класс-предок (родитель)
class People:

    def __init__(self, name, name2, surname, birth_date):
        self.name = name
        self.name2 = name2
        self.surname = surname
        self.birth_date = birth_date
        self.__parent1 = None
        self.__parent2 = None

    def make_parent(self):
        k = random.randint(1, 250)
        return People(f'Имя_p{k}', f'Отчество_p{k}', f'Фамилия_p{k}', datetime.datetime.now())





    # def __init__(self, name, name2, surname, birth_date, parent1):
    #     self.name = name
    #     self.name2 = name2
    #     self.surname = surname
    #     self.birth_date = birth_date
    #     self.parent1 = parent1
    #     self.parent2 = None
    #
    # def __init__(self, name, name2, surname, birth_date, parent1, parent2):
    #     self.name = name
    #     self.name2 = name2
    #     self.surname = surname
    #     self.birth_date = birth_date
    #     self.parent1 = parent1
    #     self.parent2 = parent2

    def get_full_name(self):
        return self.name + '\t' + self.surname

    def get_fio(self):
        return self.surname + ' ' + self.name[0] + '.' + self.name2[0]

    @property
    def parent1(self):
        return self.__parent1

    @parent1.setter
    def parent1(self, people1):
        self.__parent1 = people1

    @property
    def parent2(self):
        return self.__parent2

    @parent2.setter
    def parent2(self, people2):
        self.__parent2 = people2

# Сами классы наследуем
class Student(People):

    def __init__(self, name, name2, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, name2, surname, birth_date)
        # Добавляем уникальные атрибуты
        # self._class_room = {'class_num': int(class_room.split()[0]),
        #                     'class_char': class_room.split()[1]}
        self.school = school
        self.class_room = class_room


    # # И уникальные методы
    # @property
    # def class_room(self):
    #     return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])
    #
    # def next_class(self):
    #     self._class_room['class_num'] += 1

class Teacher(People):
    # класс учителя
    def __init__(self, name, name2, surname, birth_date, school, discipline):
        People.__init__(self, name, name2, surname, birth_date)
        self.__teach_classes = list()
        self.__discipline = discipline
        self.__school = school

    #     назначить учителя на класс
    def assign_class(self, class_room):
        if class_room not in self.__teach_classes:
            self.__teach_classes.append(class_room)
    @property
    def discipline(self):
        return self.__discipline




class ClassRoom:

    def __init__(self, school, class_num, class_char):
        self.school = school
        self.class_num = class_num
        self.class_char = class_char
        self.__teachers = list()
        self.__students = list()

    # def __init__(self, school, arr):
    #     self.school = school
    #     self.class_num = int(arr[0])
    #     self.class_char = str(arr[1])

    @property
    def students(self):
        return self.__students

    @property
    def teachers(self):
        return self.__teachers

    def __str__(self):
        return f"{self.class_num} {self.class_char}"

    def assign_teacher(self, teacher):
        if teacher not in self.__teachers:
            self.__teachers.append(teacher)

    def append_student(self, student):
        self.__students.append(student)


class School:

    def __init__(self):
        self.__class_dict = dict()
        self.__teachers = list()

    def make_class(self, num, char):
        cls = ClassRoom(self, num, char)
        self.__class_dict[str(cls)] = cls
        return cls

    def add_teacher(self, name, name2, surname, birth_date, discipline):
        teacher = Teacher(name, name2, surname, birth_date, self, discipline)
        if teacher not in self.__teachers:
            self.__teachers.append(teacher)

    def assign_teacher_to_class(self, classroom, teacher):
        teacher.assign_class(classroom)
        classroom.assign_teacher(teacher)

    def class_by_key(self, key):
        return self.__class_dict[key]

    @property
    def classes(self):
        return self.__class_dict.values()

    @property
    def teachers(self):
        return self.__teachers


def fill_data(school):

    # предварительное заполнение данными школы ))
    # для упрощения везде дату рождения генерим через now
    lst_cls = [[1, 'A'], [1, 'B'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [4, 'A'], [4, 'B'], [5, 'A'],\
               [5, 'B'], [5, 'C'], [6, 'A'], [6, 'B'], [7, 'A'], [8, 'A'], [9, 'A'], [10, 'A']]
    # создадим классы
    for i in lst_cls:
        school.make_class(i[0], i[1])
    # наймем учителей
    for i in range(15):
        school.add_teacher(f'Имя_t{i}', f'Отчество_t{i}', f'Фамилия_t{i}', datetime.datetime.now(), f'Предмет_{i}')

    # заполним их учениками
    for i in school.classes:
        for k in range(random.randint(5, 15)):
            stud = Student(f"Имя_{k}[{i}]", f"Отчество_{k}[{i}]", f"Фамилия_{k}[{i}]", datetime.datetime.now(), i.school, i)
            # заполним родителей
            stud.parent1 = stud.make_parent()
            stud.parent2 = stud.make_parent()
            i.append_student(stud)
        # распределим учителей
        for k in range(7):
            school.assign_teacher_to_class(i, school.teachers[random.randint(0, 14)])


def test2(school):
    print()
    # задание 1
    print("1. Получить полный список всех классов школы")
    print()
    print("Классы школы")
    for i in school.classes:
        print(f"Класс {i}")
    print()

    # задание 2
    print("2. Получить список всех учеников в указанном классе")
    scls = input("Введите класс (номер пробел и буква в верхнем регистре анг раскладка) : \t")
    cls = school.class_by_key(scls)
    print(f"Класс {cls}:")
    if cls is not None:
        for i in cls.students:
            print(f"Ученик {i.get_fio()}")
    print()

    # задание 3
    print("# 3. Получить список всех предметов указанного ученика")
    pup = cls.students[random.randint(0, len(cls.students)-1)]
    print(f"для ученика {pup.get_fio()} список предметов:")
    c = pup.class_room
    for k in c.teachers:
        print(f"{pup.get_fio()} --> \t{c} --> \t{k.get_full_name()} -->\t{k.discipline}")
    print()

    # задание 4
    print("# 4. Узнать ФИО родителей указанного ученика")
    print(f"Родители ученика: {pup.parent1.get_fio()} и {pup.parent2.get_fio()}")
    print()
    # задание 5
    print("# 5. Получить список всех Учителей, преподающих в указанном классе")
    print(f"В классе {cls} преподают:")
    if cls is not None:
        for i in cls.teachers:
            print(f"Преподаватель - {i.get_full_name()}")


school = School()
fill_data(school)
test2(school)

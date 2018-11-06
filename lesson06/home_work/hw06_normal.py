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

    def __init__(self, name, name2, surname, birth_date, parent1):
        self.name = name
        self.name2 = name2
        self.surname = surname
        self.birth_date = birth_date
        self.parent1 = parent1
        self.parent2 = None

    def __init__(self, name, name2, surname, birth_date, parent1, parent2):
        self.name = name
        self.name2 = name2
        self.surname = surname
        self.birth_date = birth_date
        self.parent1 = parent1
        self.parent2 = parent2

    def get_full_name(self):
        return self.name + ' ' + self.surname

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

    @parent1.setter
    def parent2(self, people2):
        self.__parent2 = people2

# Сами классы наследуем
class Student(People):

    def __init__(self, name, name2, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, surname, birth_date)
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
    def __init__(self, name, surname, birth_date, school, discipline):
        People.__init__(self, name, surname, birth_date, school)
        self.__teach_classes = list()
        self.__discipline = discipline

    #     назначить учителя на класс
    def assign_class(self, class_room):
        self.__teach_classes.append(class_room)

class School:

    def __init__(self):
        self.__class_list = list()

    def make_class(self, num, char):
        cls = ClassRoom(self, num, char)
        self.__class_list.append(cls)
        return cls

    # def make_class_arr(self, arr):
    #     cls = ClassRoom(self, arr)
    #     self.__class_list.append(cls)
    #     return cls



    @property
    def classes(self):
        return self.__class_list


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

    def __str__(self):
        return f"{self.class_num} {self.class_char}"

    def assign_teacher(self, teacher):
        self.__teachers.append(teacher)

    def append_student(self, student):
        self.__students.append(student)

school = School()
lst_cls = [[1, 'A'], [1, 'B'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [4, 'A'], [4, 'B'], [5, 'A'], [5, 'B'], [5, 'C']]
for i in lst_cls:
    # school.make_class_arr(i)
    print(school.make_class(i[0], i[1]))
print()
for i in school.classes:
    print(i)
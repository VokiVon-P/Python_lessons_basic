__author__ = 'Павел Новиков (aka Paul VokiVon)'

import random

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

class Bag:
    """
    Класс для Мешка с бочонками
    """
    __i_turn = 0
    __kegs = list()

    def __init__(self):
        self.__kegs = [i for i in range(1, 91)]

    def next_turn(self):
        if self.__i_turn <= 90:
            k = len(self.__kegs)
            i = random.randint(0, k-1)
            res = self.__kegs.pop(i)
            self.__i_turn += 1
            # print(f"i={i} \tk={k} \tres={res} \tturn={self.__i_turn}")
            return res
        else:
            return -1

    @property
    def is_empty(self):
        return len(self.__kegs) == 0

class _ItemCard:
    """
    Вспомогательный класс - элемент карточки
    """
    # flag = False
    # num = -1

    def __init__(self, number = -1, flg = False):
        self.num = number
        self.flag = flg

    def __str__(self):
        if self.num != -1:
            if self.flag:
                txt = ' - '
            else:
                txt = str(self.num).rjust(3, " ")
        else:
            txt = '   '
        return txt

    def __int__(self):
        return self.num

    def __eq__(self, other):
        return self.num == other

    def __lt__(self, other):
        return self.num < int(other)


class Card:
    """
    Класс для карточки для лото
    """

    # __card = list()
    # __num_list = list()
    # name


    def __init__(self, name):
        self.name = name
        self.__num_list_init()
        self.__show_list_init()


    def __str__(self):
        txt = self.name.center(27)
        # for k in self.__num_list:
        #     txt += str(k)
        txt += '\n'
        txt += '---------------------------\n'
        for i in self.__card:
            s = ""
            for j in i:
                s += str(j)
            txt += (s + '\n')
        txt += '---------------------------\n'
        return txt

    # заполнение значимых данных для карточки
    def __num_list_init(self):
        self.__num_list = list()

        while len(self.__num_list) < 15:
            i = random.randint(1, 90)
            ic = _ItemCard(i)
            if ic not in self.__num_list:
                self.__num_list.append(ic)

    # заполнение данных для правильного представления данных
    # вызывается после инициализиции основых данных
    def __show_list_init(self):
        self.__card = list()
        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[:5]))
        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[5:10]))
        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[-5:]))

    # служебная - создание строки карточки
    @staticmethod
    def make_show_line():
        return [_ItemCard() for _ in range(0,9)]

    # распределяет цифры по строкам карточки
    def init_show_line(self, line, numlist):
        numlist.sort()
        temp = list()
        # генерим места расположения цифр
        for _ in numlist:
            j = random.randint(0, 8)
            while j in temp:
                j = random.randint(0, 8)
            temp.append(j)
        temp.sort()
        # заполняем места цифрами
        j = 0
        for i in numlist:
            line[temp[j]] = i
            j += 1
        return line

    def has_number(self, num):
        ic = _ItemCard(num)
        return ic in self.__num_list

    def mark_number(self, num):
        self.__num_list[self.__num_list.index(_ItemCard(num))].flag = True

    def auto_mark_number(self, num):
        if self.has_number(num):
            self.mark_number(num)

    def is_win(self):
        res = True
        for i in self.__num_list:
            res = res and i.flag
        return res


def winner(card, num):
    print(''.center(27, "*"))
    print(" ПОБЕДА! ".center(27, "*"))
    print(''.center(27, "*"))
    print(f" Бочонок №: {num} ".center(27, " "))
    print()
    print(card)

def loser(card, num, ans):
    print()
    print(''.center(27, "-"))
    print(" ПОРАЖЕНИЕ! ".center(27, "-"))
    print(''.center(27, "-"))
    print(f" Бочонок №: {num} ".center(27, " "))
    print()
    print(f" Ваш ответ: {ans} ".center(27, " "))
    print()
    print(card)

def make_choice():
    ok = False
    in_num = 0
    while (not ok):
        in_str = input('  [1] - Зачеркнуть\n  [2] - Продолжить\n' + '\tВаш выбор:\t')
        if in_str.isdigit() and int(in_str) in [1, 2]:
            in_num = int(in_str)
            ok = True
        else:
            print('  [!] - Повторите выбор плз!')
    return in_num

def check_choice(card, keg, ch_num):
    res = True
    if ch_num == 1 and not card.has_number(keg):
        res = False
        loser(card, keg, "[1] - Вы зачеркнули отсутствующее на карточке число!")
    elif ch_num == 2 and card.has_number(keg):
        res = False
        loser(card, keg, "[2] - Вы пропустили число на карточке!")
    return res


bg = Bag()
my_card = Card("Моя Карточка")
comp_card = Card("Карточка Компьютера")
while not bg.is_empty:
    keg = bg.next_turn()
    print()
    print(f" Бочонок №: {keg} ".center(27, " "))
    print()
    print(my_card)
    print(comp_card)
    if not check_choice(my_card, keg, make_choice()):
        break
    my_card.auto_mark_number(keg)
    comp_card.auto_mark_number(keg)

    if my_card.is_win():
        winner(my_card, keg)
        break
    if comp_card.is_win():
        winner(comp_card, keg)
        break


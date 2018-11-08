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


class _ItemCard:
    """
    Вспомогательный класс - элемент карточки
    """
    flag = False
    num = -1

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


class Card:
    """
    Класс для карточки для лото
    """

    # __card = list()
    # __num_list = list()


    def __init__(self):
        self.__num_list = list()
        self.__num_list_init()
        self.__card = list()

        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[:5]))
        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[5:10]))
        self.__card.append(self.init_show_line(Card.make_show_line(), self.__num_list[-5:]))

        # __card[0]

    def __str__(self):
        txt = ''
        for k in self.__num_list:
            txt += str(k)
        print(txt + '\n')
        print('---------------------------\n')
        for i in self.__card:
            s = ""
            for j in i:
                s += str(j)
            print(s)
        print('---------------------------\n')
        return "OK"

    #     заполнение значимых данных для карточки
    def __num_list_init(self):
        while len(self.__num_list) < 15:
            i = random.randint(1, 90)
            if i not in self.__num_list:
                ic = _ItemCard(i)
                self.__num_list.append(ic)

    @staticmethod
    def make_show_line():
        return [_ItemCard() for _ in range(0,9)]


    def init_show_line(self, line, numlist):
        for k in numlist:
            j = random.randint(0, 8)
            while line[j].num != -1:
                j = random.randint(0, 8)
            line[j] = k
        return line







bg = Bag()
for i in range(1, 91):
    bg.next_turn()

print()
card_1 = Card()
print(card_1)
print()
mycard = Card()
print(mycard)


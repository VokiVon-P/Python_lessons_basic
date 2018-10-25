__author__ = 'Павел Новиков (aka Paul VokiVon)'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    scale = 10 ** ndigits
    num_round = number * scale + 0.5  # * добавляем соль(0,5) чтобы откорректировать разряд в будущем преобразовании в инт
    num = int(num_round)
    result = num/scale
    return result

print("---------- Задача 1 ----------")
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):

    def sum_num(numbers):
        sum = 0
        for i in numbers:
            sum += int(i)
        return sum

    numbers = str(ticket_number)
    if len(numbers) != 6:
        return "НЕВЕРНОЕ ЧИСЛО"
    sum1 = sum_num(numbers[:3])
    sum2 = sum_num(numbers[-3:])
    if sum1 == sum2:
        sresult = f"!!!LUCKY!!! {sum1} = {sum2}"
    else:
        sresult = f"-UNLUCKY- {sum1} <> {sum2}"
    return sresult

print("---------- Задача 2 ----------")
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

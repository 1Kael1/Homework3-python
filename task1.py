# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
num = input('Введи число: ')


def getRandomList(num):
    num = int(num)
    print(num, type(num))

    randomList = [i for i in range(-num, num, 3)]

    print(randomList, type(randomList))
    return randomList


def odd_summ(my_list):

    number = 0

    for j in my_list:

        print(f'Для числа j = {j} --> Индекс:{my_list.index(j)} ')

        if (my_list.index(j) % 2 > 0):

            print(f'Число {j} ({type(j)}) на НЕчетной позиции ')

            number += j

    print(f'сумма элементов на Нечетных позициях = {number} ')


my_list = getRandomList(num)
odd_summ(my_list)

# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def floatNum(arr):

   

    arrDecimal = []
    for i in arr:
        if i > 0:
            decimal = round(i%1 , 3)
        else:
            decimal = round(i % (-1), 3)
        if decimal == 0:
            continue
        arrDecimal.append(decimal)


    print(f'Дробная часть чисел на входе: {arrDecimal}') 

    maxElem = max(arrDecimal)
    minElem = min(arrDecimal)

    print(f'Разница {maxElem} и {minElem} = {round(maxElem - minElem , 3)}')

floatNum([1.1, 1.2, 3.1, 5, 10.01])
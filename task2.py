# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def my_list(arr):

    leftIdx = 0
    rightIdx = (len(arr)-1)

   
    while(leftIdx <= rightIdx):

        print(f'ЛевИндекс:{leftIdx} , ПравИндекс:{rightIdx}')

        multi = (arr[leftIdx])*(arr[rightIdx])
        print(f'ЧислоЛевое: {arr[leftIdx]}, ЧислоПравое: {arr[rightIdx]}')

        print(f'Итог умножения: {multi} \n')

        leftIdx +=1
        rightIdx -=1

my_list([2,3,5,6])
my_list([2,3,4,5,6])
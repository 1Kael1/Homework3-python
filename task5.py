#  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def calcFibi(num):
    if (num < -1):
        num = -num
        
    arr = [0,1] 
    
    count = 1
    
    while(count<num):
        if num == 1:    
            print(arr)
            break

        if num > 1:
            acc = arr[len(arr)-1] + arr[len(arr)-2]
            arr.append(acc)

            count +=1

    print(f'Числа Фибоначчи для {num} = {arr}')
    return  arr

def calcFibiNeg(negNum):
    if (negNum > -1):
        negNum = -negNum

    arrNeg = [0,1]

    count = -1

    while(count > negNum):
        if negNum == -1:
            print(arrNeg)  

        if(negNum < -1):

            acc = arrNeg[len(arrNeg)-2] - arrNeg[len(arrNeg)-1]
            arrNeg.append(acc)
            count -=1  
    print(f'Числа Фибоначчи для {negNum} = {arrNeg}')

numFibi = int(input('Введите число для расчета числа Фибоначчи: '))
calcFibi(numFibi)

calcFibiNeg(numFibi)
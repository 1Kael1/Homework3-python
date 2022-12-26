# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecToBin(dec):
    num = ''          
    while dec > 0:
        if dec % 2 == 1: 
            num += '1'   
        else:
            num += '0'
        dec //= 2          

    return num[::-1]     


decBin = int(input("Введите десятичное число: "))
print(DecToBin(decBin))

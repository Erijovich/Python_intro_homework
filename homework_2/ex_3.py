# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

from functions import input_int_number

def formula(n):
    sum = 0
    for i in range(1,n+1):        
        sum += int((1+1/i)**i)
        print(f'{i}: {sum}', end=',  ')
    print(f'\nВся сумма = {sum}')

def start():
    print()
    formula(input_int_number(invite_msg, exeption_msg))   

invite_msg = 'Введите целое число: '
exeption_msg = 'Только целые числа!'


# 1: 2,  2: 4,  3: 6,  4: 8,  5: 10,  6: 12, 

# start()
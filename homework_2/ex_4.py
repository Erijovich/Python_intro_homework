# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import os, sys
from functions import input_int_number


def start():

    print()
    n = input_int_number(invite_msg, exeption_msg)
    array = [i for i in range(-n,n+1)]

    print(f'{array} - массив чисел от {-n} до {n}')

    pos_from_file = set()
    positions = set() 
    
    # просто open не работает, обращается к директории исполнения скрипта
    # а не туда, где питоновский файл находится, инет подсказал такое вот решение
    with open(os.path.join(sys.path[0],'file.txt'), 'r') as data: 
        # не до конца огонь, конечно.. если в строчку несколько символов есть - не считает, зато от другого мусора избавит
        for line in data: pos_from_file.add(line.strip())

    mult = 1
    for i in pos_from_file:
        try: 
            num = int(i)
            positions.add(num)
            mult*=array[num]
        except Exception as error: pass # print(error) отладка
    a=list(positions)
    a.sort()
    print(a, ' - Позиции, элементы массива на которых будут перемножаться.\nОтрицательные значения позиции считаются с конца массива, выходящие за границу массива - не учитываются')
    print(f'Результат перемножения чисел массива на вышеуказаных позициях равен {mult}')

invite_msg = 'Введите целое число - границу промежутка: '
exeption_msg = 'Только целые числа!'

# start()





# Проверка
# mult = 1
# for i in positions:
#     print('Posishn = ', end='')
#     print(i, end=', num = ')
#     try: 
#         num = int(i)
#         print(num, end=', array[num] = ')
#         print(array[num], end=', mult = ')
#         mult*=array[num]
#         print(mult, end='\n')
#     except Exception as error:
#         print(f'\n{error}\n')
# print(mult)


# mult = 1
# for i in pos_from_file:
#     try: 
#         num = int(i)
#         positions.add(num)
#         mult*=array[num]
#     except Exception as error: pass
# print(positions)
# print(mult)
""" 
Задача 30: Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума) 
"""

import my_functions as mf

def ar_prog(a,d,n):
    return [a + i*d for i in range(n)]

def find_indexes(min, max, array):
    if max<min: max,min = min,max
    return [i for i in range(len(array)) if min <= array[i] <= max]

# использование enumerate() подсмотрел. тут пользы особо нет , на будущее
def find_i_enum (min, max, array):
    if max<min: max,min = min,max
    return [i for i,n in enumerate(array) if min <= n <= max]


# def qwe (lst):
#     return [len(i) for i in lst] # map

def start_test():
    print(ar_prog(7,2,5))
    print(find_indexes(5,10,[1,2,4,6,8,5,11,9,10,23]))
    print(find_i_enum(5,10,[1,2,4,6,8,5,11,9,10,23]))

def start():
    print('\nЗадачка 1')
    print(ar_prog(mf.input_int('Первый элемент последовательности: '),
                  mf.input_int('Разность последовательности: '),
                  mf.input_int('Количество элементов последовательности: ')))

    print('\nЗадачка 2')
    print(find_indexes(mf.input_int('Первая граница диапазона: '),
                       mf.input_int('Вторая граница диапазона: '),
                       mf.generate_random_int_list(mf.input_int('Размер массива: '),
                                                   mf.input_int('Максимальное значение в массиве: '),
                                                   mf.input_int('Минимальное значение в массиве: '))))

start_test()
# start()
# print(qwe(['qwe','wqeqwe','1errr']))
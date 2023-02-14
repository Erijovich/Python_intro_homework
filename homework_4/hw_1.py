# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


import my_functions as mf

def input_set(pos):
    msg_inv = 'Укажите размер {} набора: '
    msg_input = 'Введите значение элемента: '

    set_len = mf.input_int(msg_inv.format(pos))
    some_set = set()
    while len(some_set) < set_len:
        some_set.add(mf.input_int(msg_input))
    return some_set

print(sorted(input_set('первого') & input_set('второго')))


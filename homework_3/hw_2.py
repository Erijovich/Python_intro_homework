# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import my_functions as mf

def nearest_num_finder():
    msg_intro = '\nЗадачка про ближайшее число'
    msg_inv = 'Укажите размер массива: '
    msg_max = 'Укажите максимальный размер значения в массиве: '
    msg_to_find = 'Укажите искомое число: '
    msg_array = 'Сгенерированный массив: {}'

    a_total = mf.input_int(msg_inv)
    a_max = mf.input_int(msg_max)
    array = mf.generate_random_int_list(a_total,a_max)
    print(msg_array.format(array))

    user_input = mf.input_int(msg_to_find)
 
    min_diff = min({abs(i - user_input) for i in array}) # находим минимум из множества всех разниц по модулю между значениями массива и введённого числа
    return {i for i in array if abs(i - user_input) == min_diff} # делаем новое множество, на случай если два числа на одинаковом расстоянии вверх и вниз стоят

msg_answer = 'Следующие числа являются ближайшими к введённому: {}'
print(msg_answer.format(nearest_num_finder()))



# def min_difference_finder(array, number):
#   return min(array, key=lambda list_value: abs(list_value-number))


# min_diff2 = min_difference_finder(array, user_input)
# nearest_numbers = {i for i in array if abs(i - user_input) == min_diff}

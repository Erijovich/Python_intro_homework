# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


import my_functions as mf

# по сути, метод списков .count() решает всю задачу
def num_counter():
    msg_inv = 'Укажите размер массива: '
    msg_max = 'Укажите максимальный размер значения в массиве: '
    msg_to_find = 'Укажите искомое число: '
    msg_array = 'Сгенерированный массив: {}'
    msg_answer = 'Число {} в этом массиве встречается {} раз'

    n = mf.input_int(msg_inv)
    max = mf.input_int(msg_max)
    array = mf.generate_random_int_list(n,max)
    print(msg_array.format(array))
    num_to_find = mf.input_int(msg_to_find)
    
    print(msg_answer.format(num_to_find, array.count(num_to_find)))

num_counter()
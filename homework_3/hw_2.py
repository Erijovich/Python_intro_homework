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
    # хм... наверное можно сделать это словарём (а лучше вообще в отдельный файл, хм...)
    msg_intro = '\nЗадачка про ближайшее число'
    msg_inv = 'Укажите размер массива: '
    msg_max = 'Укажите максимальный размер значения в массиве: '
    msg_to_find = 'Укажите искомое число: '
    msg_array = 'Сгенерированный массив: {}'
    msg_answer = 'Следующие числа являются ближайшими к введённому: {}'
    msg_answer_solo = 'Следующее число является ближайшим к введённому: {}'

    # генерация массива по пользовательским критериям и ввод искомого числа
    a_total = mf.input_int(msg_inv)
    a_max = mf.input_int(msg_max)
    array = mf.generate_random_int_list(a_total,a_max)
    print(msg_array.format(array))
    user_input = mf.input_int(msg_to_find)

    # вариант 1
    print(msg_answer.format(min_difference_finder(array, user_input)))

    # вариант 2 через лямбду.. блин, хотел как попроще
    x = min_diff_lambda(array, user_input)
    if user_input in array:
        print(msg_answer_solo.format(user_input))
    elif x[0]-user_input == user_input-x[1]:
        print(msg_answer.format(x))
    else:
        print(msg_answer_solo.format(min(x)))
    # print(user_input if user_input in array else min_diff_lambda(array, user_input)) # нее.. три варианта выхода может быть
 
    

def min_difference_finder(array, number):
    min_diff = min({abs(i - number) for i in array}) # находим минимум из множества всех разниц по модулю между значениями массива и введённого числа
    return {i for i in array if abs(i - number) == min_diff} # делаем новое множество, на случай если два числа на одинаковом расстоянии вверх и вниз стоят



# возвращает список (можно и множество, тут не важно, наверное) первого по значению числа в массиве перед искомым и первого после искомого
def min_diff_lambda(array, number):
    return [min(filter(lambda list_value : list_value > number, array)), 
            max(filter(lambda list_value : list_value < number, array))]
            # тут ещё и min() может быть пустым -> ошибка...



nearest_num_finder()





# def min_difference_finder(array, number):
#   return min(array, key=lambda list_value: abs(list_value-number))


# min_diff2 = min_difference_finder(array, user_input)
# nearest_numbers = {i for i in array if abs(i - user_input) == min_diff}

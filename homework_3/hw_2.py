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

def min_defference(array, number):
  return min(array, key=lambda x: abs(x-number))



def nearest_num_finder():
    msg_inv = 'Укажите размер массива: '
    msg_max = 'Укажите максимальный размер значения в массиве: '
    msg_to_find = 'Укажите искомое число: '

    # n = mf.input_int(msg_inv)
    # max = mf.input_int(msg_max)
    array = mf.generate_random_int_list()
    print(f'Сгенерированный массив: {array}')

    user_input = mf.input_int(msg_to_find)




    min_diff = min_defference(array, user_input)
    print(min_diff)
    nearest_numbers = list()
    for i in array:
        print('current i = ',i, ' user_input-i = ', abs(user_input-i))
        if abs(user_input-i)==min_diff:
            nearest_numbers.append(i)
            print('this is IF i !')

    # nearest_numbers = [i for i in array if abs(user_input-i)==min_diff]

    print(f'you want this {nearest_numbers} yeah')









    # differences = {user_input-num: num for num in array} #словарь будет убирать дубли
    # print(differences)


    # min_diff = min(differences)
    # print(min_diff)
    # closest_number = differences[min_diff]
    # print (closest_number)

nearest_num_finder()





# some_array = [5, 78, 45, 12, 56, 9999]

# def nearest(lst, target):
#   return min(lst, key=lambda x: abs(x-target))

# print(nearest(some_array, 52))






# отсортировать , разделить нулём и работь с разными знаками отедльно

#  еще вариант найти ближайший в рлюс и ближайший в минус и сравнить

""" 

a, n, find_num = [int(i) for i in input().split()], int(input()), 100
for i in range(len(a)):
    if a[i] < n:
        find_num = -find_num
    else:
        find_num = find_num + 0
    if a[i] >= n and a[i] - n <= find_num - n:
        find_num = a[i]
    elif a[i] <= n and find_num - n <= a[i] - n:
        find_num = a[i]
print(find_num)
 """
""" 

попробовать список ключей сравнивать с нулём искать ближайшее
потом сравнивать по модулю
и искать есть ли его брат близнец со знаком минус



my_list = [int(input('type element: ')) for i in range(int(input('type amount: ')))]
x = int(input('type X: '))
if x in my_list:
    print(x) # если х есть в изначальном списке то его и выводим
else:
    my_list.append(x) # добавили в первый список значение Х
    my_list = sorted(my_list) # отсортировали список от меньшего к большему
    if my_list.index(x) == len(my_list) - 1: # если искомый элемент самый большой
        element2 = my_list[my_list.index(x) - 1] # ближайший слева элемент к искомому
        print(element2)
    elif my_list.index(x) == 0: # если искомый элемент самый маленький
        element = my_list[my_list.index(x) + 1] # [1] ближайший справа элемент к искомому
        print(element)
    else: # если искомый элемент в середине, выводим оба соседних с ним элемнта
        element = my_list[my_list.index(x) - 1] # ближайший слева элемент к искомому
        print(element)
        element2 = my_list[my_list.index(x) + 1] # ближайший справа элемент к искомому
        print(element2)

 """



# print('\nЗадачка про ближайшее число')
# print(array)
# to_find = int(input('Какое ближаёшее ищем? '))

# diff = ((array[0] - to_find)**2)**0.5
# for i in range(1,len(array)):



# up_dif = array[0] - to_find
# down_dif = to_find - array[0]
# for i in range(1,len(array)):
#     if array[i] - to_find < up_dif and array[i] - to_find > 0: up_dif = array[i] - to_find
#     if to_find - array[i] < down_dif and to_find - array[i] > 0: down_dif = to_find - array[i]

# if up_dif==down_dif: print(up_dif, down_dif)
# else:
#     if  up_dif<down_dif:
#         print(up_dif)
#     else: print(down_dif)

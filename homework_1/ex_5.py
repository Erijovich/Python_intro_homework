# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Реализовал общий случай данной задачи для N-мерного пространства и способ задания координат руками или псевдорандомом

# ох, понаписал, ну, намудрил.... 
# У проверяющего заочно прошу прощения, не мог остановиться, такое ощущение, что, чем
# больше функционала добавляешь, тем больше нужно ещё добавить - проверки, защиты, украшательства, всё подряд....


import random

#  Защита от ввода не чисел (слов, знаков)
def input_float_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try: return(float(user_input))   
    except: print(exeption_msg)
    return input_float_number(invite_msg, exeption_msg)  

#  Защита от ввода не ЦЕЛЫХ чисел (слов, знаков, вещественных чисел)
def input_int_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try: return(int(user_input))   
    except: print(exeption_msg)
    return input_int_number(invite_msg, exeption_msg)  

# генерация одномерного массива с заданными значения минимума, максимума, общего количества элементов, и кол-ва знаков после запятой
def create_random_list(min, max, total, accuracy):
    list = [round((min + (max-min)*random.random()), accuracy) for i in range(total)]
    return list

# расчёт расстояния, на вход подаются списки с координатами и размерность пространства.
# Важно! размеры списков должны совпадать и соответсвовать размерности
# По сути - это решение, пара строк, всё остальное лишь надстройки, хех
def calculate_total_distance(a, b, dimension):
    distance = 0
    for i in range(dimension):
        distance += (a[i] - b[i])**2
    return distance**(0.5)

# Ввод псевдорандомом
def calculate_with_random(dimension):
    # Диапазон значений координат
    print('\nВведите диапазон значений координат')
    min = input_float_number('Минимальное значение: ', exeption_msg_float)
    max = input_float_number('Максимальное значение: ', exeption_msg_float)
    if max<min:
        print('Хорошая попытка, мистер тестировщик, меняю значения минимума и максимума!')
        min,max = max,min
    accuracy = input_int_number('Сколько знаков после запятой? ', exeption_msg_natural)
    if accuracy < 0: accuracy = 0 # будем считать так)

    a_coordinate = create_random_list(min,max, dimension, accuracy)
    b_coordinate = create_random_list(min,max, dimension, accuracy)
    print(f'\nКоординаты первой точки {a_coordinate},\nКоординаты второй точки {b_coordinate}')

    return (calculate_total_distance(a_coordinate, b_coordinate, dimension))

# Ввод ручками
def calculate_with_input(dimension):
    a_coordinate = []
    b_coordinate = []
    for i in range(dimension): a_coordinate.append(input_float_number(f'Введите {i+1}-ю координату первой точки: ', exeption_msg_float))
    print()
    for i in range(dimension): b_coordinate.append(input_float_number(f'Введите {i+1}-ю координату второй точки: ', exeption_msg_float))
    print(f'\nКоординаты первой точки {a_coordinate},\nКоординаты второй точки {b_coordinate}')

    return (calculate_total_distance(a_coordinate, b_coordinate, dimension))

# Инициализация, выбор типа ввода
def distance_calculator ():

    # Выбор размерности пространства
    print()
    flag = True
    dimension = 0
    while flag:
        dimension = input_int_number('Введите размерность пространства: ', exeption_msg_natural)
        if dimension < 1: print('Так не получится... Пространства с нулевым или отрицательным '
                                'количеством измерений мы пока не придумали. Вроде бы...')
        else: flag = False  

    # Выбор способа ввода данных
    print()
    flag = True
    input_type = 1
    while flag: 
        input_type = input('Выберите способ ввода координат точек: 1 - вручную или 2 - псевдорандомом: ')
        if input_type == '1' or input_type == '2': flag = False
        else: print('Пожалуйста выберите опцию 1 или 2')    
    print()

    #  считаем 
    total_distance = 0
    if input_type == '1': total_distance = calculate_with_input(dimension)
    elif input_type == '2': total_distance = calculate_with_random(dimension)
    else: print('Что-то пошло не так... По-хорошему, это сообщение не должно никогда возникать')    

    print(f'Расстояние между этими точками в {dimension}-мерном пространстве равно {total_distance}\n')



#  Основная программа

print('\n Эта программа принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. '
      'Ввод координат можно осуществить или руками или псевдорандомом.')

invite_msg = 'Введите координату: '
exeption_msg_natural = 'Нужно натуральное число..'
exeption_msg_float = 'Необходимо ввести вещественное число...'
flag = True

while flag:
    distance_calculator()
    continue_check = input('Повторим? 1 - да, любой другой ввод - выход: ')
    if continue_check != '1': flag = False
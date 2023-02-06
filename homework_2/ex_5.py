# Реализуйте алгоритм перемешивания списка.




# пробегаем по списку, меняем i-ый и рандомный номер
# добавляем использованные координаты во второй список
# если i-ый натыкается на использованный номер - пропускаем
# если рандом натыкается на использованный - тоже пропускаем

from functions import generate_random_int_list
from functions import input_int_number
import random

msg_total = 'Введите размер списка: '
msg_bound = 'Введите границу списка: '
msg_exep = 'Только целые числа!'


def start():

    print()
        

    print(f'Алгоритм перемешивания списка INT чисел, но он также подходит и для любых типов элементов')

    array = generate_random_int_list() #input_int_number(msg_total),input_int_number(msg_bound),input_int_number(msg_bound))
    print('Сгенерированный список:\n', array)

    # positions = [i for i in range(len(array))]
    # print(positions) ###
    # print(len(array)//2)
    # for i in range(len(array)//2):
    #     print('i - ', i)
    #     positions.pop(i)
    #     new_rand = positions.pop(random.choice(positions))
    #     print('rand - ', new_rand)
    #     array[i], array[new_rand] = array[new_rand], array[i]
    #     print('pozishns - ', positions)
    #     print('array - ',array)


    # for i in positions:
    #     print('i - ', i)
    #     positions.pop(i)
    #     new_rand = positions.pop(random.choice(positions))
    #     print('rand - ', new_rand)
    #     array[i], array[new_rand] = array[new_rand], array[i]
    #     print('pozishns - ', positions)
    #     print('array - ',array)



    # generated_list = [random.randint(min, max) for i in range(total)]

        #  заранее составить карту обмена (рандомно накидать список позиций)


    # for i in range(len(array)):
    #     new_rand = random.choice(positions)


    # В лоб! может быть орчень долго
    s = list()
    while len(s)< len(array):
        l = random.randrange(len(array))
        print(l)
        if l not in s:
            s.append(l)
        print(s)

    print(s)

# start()
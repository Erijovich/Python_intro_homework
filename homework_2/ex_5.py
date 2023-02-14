# Реализуйте алгоритм перемешивания списка.




# пробегаем по списку, меняем i-ый и рандомный номер
# добавляем использованные координаты во второй список
# если i-ый натыкается на использованный номер - пропускаем
# если рандом натыкается на использованный - тоже пропускаем

from functions import generate_random_int_list
from functions import input_int_number
import random

# В лоб! может быть орчень долго
# использован список, а не множество , что бы позиции остались разрозненными
def generate_random_map(array):  
    map = list()
    while len(map)< len(array):
        item = random.randrange(len(array)) 
        if item not in map:
            map.append(item)
    return map


def rearrange_list(array, map):
    rearranged_list = list(range(len(array)))
    j=0
    for i in map:
        rearranged_list[i] = array[j]
        j+=1
    return(rearranged_list)



def start():  
    print(f'Алгоритм перемешивания списка INT чисел, но он также подходит и для любых типов элементов')

    # array = generate_random_int_list() 
    array = generate_random_int_list(input_int_number(msg_total),input_int_number(msg_bound),input_int_number(msg_bound))
    print('Сгенерированный список:\n', array)
    print('Карта индексов:\n', map:=generate_random_map(array))
    print('Перемешанный список:\n', rearrange_list(array, map))


msg_total = 'Введите размер списка: '
msg_bound = 'Введите границу списка: '
msg_exep = 'Только целые числа!'

# start()


# тут надо попробовать идти не по списку а по его срезу
# что-то с позицией здесь, хочется, что бы перемешивание совершалось за количество_элементов/2 действий,
# и все элементы гарантированно меняли место
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


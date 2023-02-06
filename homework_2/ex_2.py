# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from functions import input_int_number

# Решение без использования листов
def factorial_no_list(n):
    fact = 1
    print('[', end='')
    for i in range(1, n + 1):
        fact *= i
        print(fact, end=', ')
    print(']')


def start():
    print()
    n = input_int_number(invite_msg, exeption_msg)
    if n<0: n=-n # Убираем возможный минус
    print(f'Список произведений (факториалов) чисел от 1 до {n}: ', end=' ')
    # print(factorial_list(n))
    factorial_no_list(n)

invite_msg = 'Введите натуральное число: '
exeption_msg = 'Только натуральные числа!'

# start()



# 
def factorial_list(n):
     fact_list = []
     fact = 1
     for i in range(1, n + 1):
          fact *= i
          fact_list.append(fact)
     return fact_list

# через рекурсию
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

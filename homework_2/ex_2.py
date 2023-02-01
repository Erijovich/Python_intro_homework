# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_natural_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try:
        if int(user_input) > 0:
            return(int(user_input))
        print(exeption_msg)       
    except ValueError:
        print(exeption_msg)

    return input_natural_number(invite_msg, exeption_msg)  


def factorial_list(n):
     fact_list = []
     fact = 1
     for i in range(1, n + 1):
          fact *= i
          fact_list.append(fact)
     return fact_list

invite_msg = 'Введите натуральное число: '
exeption_msg = 'Только натуральные числа!'
print(f'Список произведений чисел 1 до N: {factorial_list(input_natural_number(invite_msg, exeption_msg))}')
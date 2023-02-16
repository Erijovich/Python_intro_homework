""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4 """

def input_int (invite_msg = 'Input integer number: ', exeption_msg = 'INT numbers only!'):
    while True:
        user_input = input(invite_msg)
        if user_input.lstrip('-+').isdigit(): return(int(user_input)) 
        else: print(exeption_msg)

def rec_mult(a,b):
    return a*rec_mult(a, b-1) if b > 1 else a

def rec_sum(a,b):
    return rec_sum(max(a,b)+1, min(a,b)-1) if min(a,b)>0 else max(a,b)
# тут мин и макс использую, что бы уменьшить количество создаваемых реккурсий
# для отрицательных чисел интересно будет подумать..

print(rec_mult(input_int('Число '),input_int(' возводим в степень ')))
print(rec_sum(input_int('Число '),input_int(' суммируем с числом ')))

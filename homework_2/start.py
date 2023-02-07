import os
import ex_1, ex_2, ex_3, ex_4, ex_5
from functions import input_int_number

tasks_list = {
    1: 'Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.',
    2: 'Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.',
    3: 'Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.',
    4: 'Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение'
       + ' элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.',
    5: 'Реализуйте алгоритм перемешивания списка.'
             }

msg_intro = 'Домашняя работа №2\nкурс "знакомство с языком Python"'
msg_start = 'Пожалуйста, выберите номер задания. Нажатие любой другой клавиши позволит закончить выполнение программы\nНомер задания: '
msg_fin = 'Вы хотите завершить программу? 1 - нет, любой другой ввод - да: '
msg_goodbye = 'Вы завершили работу программы, bye-bye'

os.system('cls')
print()
print(msg_intro)
for i in tasks_list: print(f'{i}) {tasks_list[i]}')
flag = True
while flag:
    print()    
    user_choise = input(msg_start)
    match user_choise:
        case '1': ex_1.start()
        case '2': ex_2.start()
        case '3': ex_3.start()
        case '4': ex_4.start() 
        case '5': ex_5.start()
        case _: 
            if input(msg_fin) != '1': flag = False
    print('Конец задачи')
print(msg_goodbye)
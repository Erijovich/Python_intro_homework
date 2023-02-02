# Урок 1. Ввод-Вывод, операторы ветвления
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def input_day():
    a = (input('Введите номер дня недели - '))
    try:
        return int(a)
    except:
        print('Нужно ввести целое число от 1 до 7')
        return input_day()

def check_day():
    a = input_day()
    if 0<a<6:
        return 'будень'
    elif 5<a<8:
        return 'выходной'
    else:
        print('Нужно ввести целое число от 1 до 7')
        return check_day()

print('\nЭта программа принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.\n')
print(check_day())
print()
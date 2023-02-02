# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# сделал функцию чуть более универсальной
def input_int_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try: return(int(user_input))   
    except: print(exeption_msg)
    return input_int_number(invite_msg, exeption_msg)  


print('\nЭтa программа по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)\n')

invite_msg = 'Введите номер четверти (от 1 до 4): '
exeption_msg = 'Нужно натуральное число в диапазоне от 1 до 4..'
a = 0
flag = True

while flag:
    a = input_int_number(invite_msg, exeption_msg)
    if 0<a<=4: flag = False
    else: print(exeption_msg)

text = ''
if  a == 1: text = 'x > 0, y > 0'
elif a == 2: text = 'x < 0, y > 0'
elif a == 3: text = 'x < 0, y < 0'
elif a == 4: text = 'x > 0, y < 0'

print(f'\nB {a} четверти диапазон возможных координат будет следующим: {text}\n')
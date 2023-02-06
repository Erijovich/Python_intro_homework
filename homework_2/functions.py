import random

# Функция пробует привести введённое что-то в тип int
# при невозможности пишет сообщение (exeption_msg) и запускается снова
def input_int_number (invite_msg = 'Input int number: ', exeption_msg = 'INT numbers only!'): # int число
    user_input = input(invite_msg)
    try: return(int(user_input))   
    except ValueError: print(exeption_msg)
    return input_int_number(invite_msg, exeption_msg)  

# приведение к типу float
def input_float_number (invite_msg = 'Input float number: ', exeption_msg = 'FLOAT numbers only!'):
    user_input = input(invite_msg)
    try: return(float(user_input))   
    except ValueError: print(exeption_msg)
    return input_int_number(invite_msg, exeption_msg)  



# Функция возвращает список заданого размера (10 по умолчанию) с рандомными int числами из заданного диапазона (0-100 по умолчанию)
# Длина списка фиксирована
# total - размерность массива, по умолчанию 10, если задано отрицательное значение - меняет на положительное
# min - минимум диапазона (порядок не важен)
# max - максимум диапазона (порядок не важен)
def generate_random_int_list(total = 10, max = 100, min = 0):
    if max<min: min,max = max,min
    if total < 0: total = -total
    return [random.randint(min, max) for i in range(total)]

# float список
# Длина списка фиксирована
def create_random_float_list(total = 10,max = 100, min = 0, accuracy = 2):
    if max<min: min,max = max,min
    if total < 0: total = -total
    if accuracy < 0: accuracy = 0
    return [round((min + (max-min)*random.random()), accuracy) for i in range(total)]

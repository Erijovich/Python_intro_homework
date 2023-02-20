import my_functions as mf
import os

def create_operation_table(fn, rows=6, cols=6):
    if not 1 < rows < 21: rows = 6 
    if not 1 < cols < 21: cols = 6 # защита от превышающих
    return [[fn(i+1,j+1) for j in range(cols)] for i in range(rows)]
    
def print_table(table):
    print()
    for row in table:
        for num in row: 
            print('{:^4}'.format(num), end=' ')
        print()
    print()

def input_conditions():
    print(msg['make'])
    rows, cols = mf.input_int(msg['rows']), mf.input_int(msg['cols'])
    counter = 0
    while True:
        print(msg['operations'], *oper_shop.keys())
        operation = input(msg['op_choise'])
        if operation in oper_shop:  # календарь, ремни, ножи
            return create_operation_table(oper_shop[operation], rows, cols)
        counter +=1
        print(msg['error'] if counter%3 != 0 else msg['megaerror'])

def start():
    print(msg['intro'])
    while True:
        print_table(input_conditions())
        if input(msg['again']) != '1': return
        os.system('cls')

# можно ли ключ подставлять в формулу? тогда не словарь , а список операций, который потом формулу делает
oper_shop = {'+': lambda x, y: x+y,
             '-': lambda x, y: x-y,
             '*': lambda x, y: x*y,
             '/': lambda x, y: x/y,
             '//': lambda x, y: x//y,
             '%': lambda x, y: x%y,
             '**': lambda x, y: x**y}

msg = {'intro': '\nСие нечто выводит таблицу бинарных операций',
       'make': 'Задай размер таблицы и выберите операцию',
       'rows': 'Укажи количество строк: ',
       'cols': 'Укажи количество столбцов: ',
       'operations': 'Доступны следующие бинарные операции: ',
       'op_choise': 'Выбери операцию: ',
       'error': 'Нет такой операции 😐 Смотри внимательно ☝',
       'again': 'Повторим? Жми 1 для повторения, любой другой ввод - завершение: ',
       'bye': 'Покеда! ✌',
       'megaerror': '\n😡 😡 😡  Ты издеваешься что ли???  👉😣\n'
      }


start()



#################################################################
#######---> ----------------------------------------- <---#######
####---->>> Подвал не законченных или не удачных идей <<<----####
#######---> ----------------------------------------- <---#######
#################################################################



def create_operation_table_boring(operation, rows=6, cols=6):
    table = [[0]*cols for i in range(rows)]
    # print(table)
    for i in range(rows):
        for j in range(cols):
            table[i][j] = operation(i+1,j+1)
    return table

def print_table_wtf(table):
    # l = 1 + len(str(max(max(table)))) # вычислияем самое длинное значение.. с минусами работать не будет.. 
    # # не так, тут проще развернуть таблицу в моносписок и тогда уже найти самое длинное число
    # print(l)
    output = '{:^5}' # как на лету менять длину поля????
    for row in table:
        for num in row: 
            print(output.format(num), end='')
        print()


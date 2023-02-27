import controller as con

def still_running():
    operation = input(msg['next_input']).strip().lower()
    while operation not in (oper_list):
        print(msg['error'])
        operation = input(msg['next_input']).strip().lower()
    return con.choose_action(operation) # choose action возвращает только тру или фолс

def print_help():
    print()
    print(msg['help'])
    for i in oper_list:
        print(f'   {i} - {oper_list[i]}')
    print()

oper_list = {
            'p': 'Вывести всю телефонную книгу на экран',
            'f': 'Найти контакт(ы) по слову(части слова) или номеру(части номера)',
            'a': 'Добавить новый контакт',
            'd': 'Удалить контакт',
            'c': 'Изменить контакт',
            'h': 'Вывести на экран помощь по командам',
            'x': 'Сохранить изменения и завершить работу программы',
            }
    
msg = {
        'next_input':   '>>> ',
        'error':        'Команда - инвалид! Что бы вывести на экран помощь по командам нажмите "h"',
        'help':         'Список доступных команд (латинскими буквами):'
      }   
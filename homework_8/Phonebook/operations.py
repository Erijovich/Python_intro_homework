import os, sys

def global_import():
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'r', encoding='utf-8') as data: 
        wrapper = data.readlines()
        for id in range(len(wrapper)):
            phonebook.append(wrapper[id].split())

def global_export():
    phonebook.sort()
    for i in phonebook[:]: # удаление пустых строк, коли такие будут. Может логичнее отправить это в импорт, хз
        if ''.join(i).strip() == '':
            phonebook.remove(i)
    with open(os.path.join(sys.path[0],'phonebook.txt'), 'w+', encoding='utf-8') as data:
        for contact in phonebook:
            data.writelines(' '.join(contact) +'\n')

def add_contact(new_contact):
    phonebook.append(new_contact)

def find_contact(some_string):
    merged = [''.join(i) for i in phonebook]
    return [index for index,contact in enumerate(merged) if some_string in contact.lower()]
    
def check_index(id, text):
    if id-1 not in range(len(phonebook)):
        print(msg['wrong_num'])
        return False
    print(f'Вы действительно хотите {text} запись "', end ='') # text = удалить или изменить
    print(*phonebook[id-1], end='"?\n') # не хочет разворачивать список в форматированном выводе, приходится в две строчки..
    return True if input('y/n - ') == 'y' else False

def del_contact(id):
    if not check_index(id, 'удалить'): return 
    phonebook.pop(id-1)

def change_contact(id):
    if not check_index(id, 'изменить'): return 
    for i in range(len(phonebook[id-1])):
        new_value = input(msg['new_value'].format(phonebook[id-1][i]))
        if new_value: 
            phonebook[id-1][i] = new_value

def print_list(contact_list):
    if not contact_list: contact_list = range(len(phonebook))
    print()
    for i in contact_list:
        print(i+1, end=' - ')
        print(*phonebook[i])
    print()


phonebook = list()
global_import()
msg = {
    'wrong_num':'Нет такого номера',
    'new_value':'Введите новое значение вместо "{}". Пустой ввод - не изменять это значение: '
      }


#################################################################
#######---> ----------------------------------------- <---#######
####---->>>          комментарии по функциям          <<<----####
#######---> ----------------------------------------- <---#######
#################################################################

# global_import()
# заполняем словарь значениями из тхт
# интересно.. здесь генератор не хочет работатть.. почему??
# phonebook = [wrapper[id].split() for id in range(len(wrapper))]

# global_export()
# тут всё сортируем по первоуму значению (фамилия) выгружаем в файл (эдакое сохранение)
# а ещё удаляем пустые строчки

# find_contact(some_string)
# возвращает индексы контактов найденных

# print_list(contact_list)
# выводит в консоли контакты по индексам
# если contact_list = False, то выводит всё книгу

# check_index(id, text)
# Проверяет есть ли введённый номер записи в списке и спрашвает подтверждения на действие (удалить , изменить)

# add_contact(new_contact)
# добавляет в конец списка новый контакт

# change_contact(id)
# чёт нагруженная сильнго получилась...

# def input_int 
# Функция пробует привести введённое что-то в тип int
# при невозможности пишет сообщение (exeption_msg) и запускается снова
# def input_int (invite_msg = 'Укажите номер записи: ', exeption_msg = 'Необходимо указать номер записи цифрами!'):
#     user_input = input(invite_msg).strip()
#     try: return(int(user_input))   
#     except ValueError: print(exeption_msg)
#     return input_int(invite_msg, exeption_msg)  
# похоже, она тут и не нужна...

# def find_contact(some_string):
#     return [index for index,contact in enumerate(phonebook) if some_string in contact]
# искал только точное совпадение слова, теперь же ищет часть слова и игнорирует заглавность букв
# сначала каждый контакт сливаем в одну строчку, затем ищем вхождения
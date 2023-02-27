import operations as ops
import user_interface as ui

# как бы вот значения ключей из словаря в UI здесь использовать, что бы не дублировать...
def choose_action(action):
    match action:
        case 'a':
            new_contact = contact_info()
            ops.add_contact(new_contact)
            print(msg['added'])
        case 'f': 
            found_contacts = ops.find_contact(input(msg['to_find']).strip().lower())
            if found_contacts: # только если список найдёнышей не пустой, тогда выводим найденное и предлагаем удалить или изменить
                print(msg['found'])
                ops.print_list(found_contacts)
            else: print(msg['not_found'])
        case 'd':
            user_input = input(msg['to_del'])
            if user_input.isdigit():
                ops.del_contact(int(user_input))
                print(msg['deleted'])
        case 'c':
            user_input = input(msg['to_del'])
            if user_input.isdigit():
                ops.change_contact(int(user_input))
        case 'p':
            ops.print_list(False)
        case 'h':
            ui.print_help()
        case 'x':
            ops.global_export()
            return False # Сохранение и выход
        case _:
            print(msg['error'])
    return True

# TODO тут хочется проверок на корректность ввода добавить.
# А так же несколько слов в одной строчке - не очень, если надо будет вычленять отдельно фамилию, имя и тд
def contact_info():
    return [
            input(msg['surname']).strip(),
            input(msg['name']).strip(),
            input(msg['fathers_name']).strip(),
            input(msg['phonenumber']).strip()
            ]

msg = {
        'to_find':      'Для поиска введите имя, фамилию или номер телефона: ',
        'surname':      'Фамилия: ',
        'name':         'Имя: ',
        'fathers_name': 'Отчество: ',
        'phonenumber':  'Номер телефона: ',
        'error':        'Invalid command! Что бы вывести на экран помощь по командам нажмите "h"',
        'found':        'Вот, что было найдено:',
        'not_found':    'Ничего не найдено',
        'to_del':       'Укажите номер записи для удаления (ввод НЕ числа - отмена команды): ',
        'to_change':    'Укажите номер записи для изменения (ввод НЕ числа - отмена команды): ',
        'added':        'Контакт успешно добавлен!',
        'deleted':      'Контакт успешно удалён!'
      }





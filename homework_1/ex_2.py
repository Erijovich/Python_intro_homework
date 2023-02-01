# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def input_bool_num(text):
    a = (input(text))
    try:
        if 0 <= int(a) < 2:
            return bool(int(a))
        else:
            print('Нужно ввести 1 или 0')
            return input_bool_num(text)
    except:
        print('Нужно ввести 1 или 0')
        return input_bool_num(text)

print('\nЭта программа проверяет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех введённых значений предикат.\n')
x = input_bool_num('Введите Х: ')
y = input_bool_num('Введите Y: ')
z = input_bool_num('Введите Z: ')
print()

if (not (x or y or z)) == ((not x) and (not y) and (not z)):
    print ('true')
else:
    print ('false')

print ('\nЕсли присмотреться внимательно: в левой части, если хотя бы одно значение истинно, то вся часть ложна, '
     + 'в правой же части точно так же, если хотя бы одно значение истинно , то через отриание оно ложно '
     + 'и через логическое и, всё выражение ложно. Таким образом, всё выражение всегда будет true\n')
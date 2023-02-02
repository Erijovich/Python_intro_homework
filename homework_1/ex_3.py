# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def num_input (text):
    a = input(text)
    try:
        return(float(a))
    except:
        print("Нужно имено число!")
        return num_input(text)

print('\nЭта программа принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, '
      'в которой находится эта точка (или на какой оси она находится). Причём в условии не понятно, зачем ограничивать '
      'равенство нулю для координат, если далее по условию, необходимо включить в проверку нахождение точки на оси\n')

x = num_input('Введите координату X: ')
y = num_input('Введите координату Y: ')

# брррр.... можно же лучше, не?
text = ''
if   x>0 and y>0:    text = 'в первой четверти'
elif x<0 and y>0:    text = 'во второй четверти'
elif x<0 and y<0:    text = 'в третьей четверти'
elif x>0 and y<0:    text = 'в четвёртой четверти'
elif x==0 and y==0:  text = 'в начале координат' 
elif x==0 and y!=0:  text = 'на оси ординат'
elif x!=0 and y==0:  text = 'на оси абсцисс'

print(f'Точка с координатами ({x}, {y}) лежит {text}')

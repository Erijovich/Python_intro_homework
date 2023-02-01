# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# Реализовал общий случай данной задачи для N-мерного пространства и способ задания координат руками или псевдорандомом

def input_float_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try: return(float(user_input))   
    except: print(exeption_msg)
    return input_float_number(invite_msg, exeption_msg)  

def input_int_number (invite_msg, exeption_msg):
    user_input = input(invite_msg)
    try: return(int(user_input))   
    except: print(exeption_msg)
    return input_int_number(invite_msg, exeption_msg)  



print('\n Эта программа принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. '
      'Ввод координат можно осуществить или руками или псевдорандомом.\n')

invite_msg = 'Введите координату: '
exeption_msg = 'Необходимо ввести вещественное число...'
a = 0


# Выбор размерности пространства
print()
flag = True
while flag:
    dimension = input_int_number('Введите размерность пространства: ', 'Нужно натуральное число..')
    if dimension < 1: print('Так не получится... Пространства с нулевым или отрицательным количеством измерений мы пока не придумали. Вроде бы...')
    else: flag = False

# Выбор способа ввода данных
print()
flag = True
input_type = 1
while flag: 
    input_type = input('Выберите способ ввода данных: 1 - вручную или 2 - псевдорандомом: ')
    if input_type == '1' or input_type == '2': flag = False
    else: print('Пожалуйста выберите опцию 1 или 2')

# Диапазон значений координат
print('\nВведите диапазон значений координат')
min = input_float_number('Минимальное значение:', exeption_msg)
max = input_float_number('Максимальное значение:', exeption_msg)
if max<min:
    print('Хорошая попытка, мистер тестировщик, меняю значения минимума и максимума!')
    temp = max
    max = min
    min = temp




""" 

    int[] a = CreateArray(n, min, max);      // точка а в n-мерном пространстве
    string list = string.Join(", ", a);
    Console.WriteLine($"Координаты первой точки:\n({list})");

    int[] b = CreateArray(n, min, max);      // точка b в n-мерном пространстве
    list = string.Join(", ", b);
    Console.WriteLine($"Координаты второй точки:\n({list})");

    Console.WriteLine($"Длина вектора = {VectorLength(a, b)}");

}


int[] CreateArray(int n, int min, int max) // создание массива размера n и заполнение целыми числами из диапазона min..max
{
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) arr[i] = new Random().Next(min, max);
    return arr;
}


double VectorLength(int[] a, int[] b) // длина отрезка между двумя заданными точками в N-мерном пространстве
{
    int sum = 0;
    int length = a.Length;
    for (int i = 0; i < length; i++) sum += (a[i] - b[i]) * (a[i] - b[i]);
    return Math.Sqrt(sum);
}


int[] CreateArray(int n, int min, int max) // создание массива размера n и заполнение целыми числами из диапазона min..max
{
    if (max < min)  // проверка и защита
    {
        int temp = min;
        min = max;
        max = temp;
    }

    var rand = new Random();
    int[] array = new int[n];
    for (int i = 0; i < n; i++) array[i] = rand.Next(min, max+1); // заполнение массива, не забывая, что справа плюс 1 к диапазону
    return array;
}


 """
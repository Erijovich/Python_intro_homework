# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12



# как-то через одно место получилось.. 

def Start_scrabble(all_dicts):
    print('\n' + msg_intro)
    while True:
        scrabble(all_dicts)
        if input(msg_again) != '1': break
        print()
    print(msg_bye)

# чувствую, это можно сделать оптимальнее.. и check_language и sum_letters имеют одни и те же параметры, нельзя ли как-то совместить?
def scrabble(all_dicts):
    user_input = input(msg_inv).upper()
    for current_dict in all_dicts:
        if check_language(user_input, current_dict):
            print(msg_answer.format(sum_letters(user_input, current_dict)))
            return
    print(msg_mixed_word)

def check_language(word_to_check, some_dict):
# Тут я делаю единое множество всех значений, потому как не представляю, как мделать так, что бы была проверка
# на слово исключительно в одном словаре (рус, англ, а может ещё немецкий или франузский добавится)
    alpabet = set()
    for item in list(some_dict.values()): alpabet |= item   
    for i in word_to_check: # как раз тут хотелось напрямую работать с элементами значений словаря
        if i not in alpabet: # типа ```for i in some_dict.values():``` что бы не "разворачивать" алфовит
            return False
    return True

# на входе искомое слово и соответствующий словарь, для каждой буквы из слова пробегаем по значениям в словаре и добавляем очко, когда находится буква
def sum_letters(word_to_sum, some_dict):
    word_value = 0
    for letter in word_to_sum:
        for key in some_dict:
            if letter in some_dict[key]:
                word_value += key
                break
    return word_value

################------------------------################
################           MAIN         ################
################------------------------################

# хочется в словарь ещё засунуть идентефикатор словаря, помимо только ценностей букв. что б прям всё максимально гибко было
dict_rus = {1: {'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'},
            2: {'Д', 'К', 'Л', 'М', 'П', 'У'},
            3: {'Б', 'Г', 'Ё', 'Ь', 'Я'},
            4: {'Й', 'Ы'},
            5: {'Ж', 'З', 'Х', 'Ц', 'Ч'},
            8: {'Ш', 'Э', 'Ю'},
            10:{'Ф', 'Щ', 'Ъ'}}

dict_eng = {1: {'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'},
            2: {'D', 'G'},
            3: {'B', 'C', 'M', 'P'},
            4: {'F', 'H', 'V', 'W', 'Y'},
            5: {'K'},
            8: {'J', 'X'},
            10:{'Q', 'Z'}}

msg_intro = 'Эта программка поможет подсчитать ценность слова в игре Scrubble'
msg_inv = 'Введите слово: '
msg_mixed_word = 'Слово должно быть одно и состоять или только из букв выбранных словарей (рус, англ)!' 
msg_answer = 'Ценность введённого слова составляет {} очков'
msg_again = 'Повторим? 1 - да, любой другой ввод - нет: '
msg_bye = 'Покеда'


Start_scrabble((dict_rus, dict_eng)) # посылаем в старт "игры" tuple тех словарей, с которыми
                                     # хотим работать. можно отдельно обозначить
                                     # думаем с запасом - словарей может быть десяток =)


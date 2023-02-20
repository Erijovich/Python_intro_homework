from random import randint, choice, choices

# ['пара-ра-рам', 'рам-пам-папам', 'па-ра-па-дам']
def ritm_checker(word_list):
    ritms = list()
    for word in word_list:
        counter = 0
        for letter in vowels: counter += word.count(letter)
        ritms.append(counter) 
        if len(ritms) == 1: continue
        if ritms[-1] != ritms[-2]: 
            print(f'слоги: {ritms}') # >debug
            return False # что бы не проверять стишком из тысячи слов, если второе уже будет не в ритм. Э - экономия
    return True

def chant_generator():
    new_chant = str()
    word_len = randint(2,4)

    for row in range(randint(2,4)):
        # устанвливаем список букв используемых в строчке (строчек 1-4 шт), на результат не влияет
        current_letters = [choice(consonants_mini) for _ in range(3)] + ['-'] # BMO
        current_letters.insert(2, choice(vowels))

        for word in range(randint(1,2)): # кол-во слов в строчке, на результат не влияет
            new_word = str()
            new_word_len = choices([word_len, word_len + 1], weights=(90,10), k =1) # кол-во слогов в слове, влияет на результат
            for syllable in range(new_word_len[0]): 
                new_word += syllables_generator(current_letters)
            new_word = new_word.rstrip('-') # убрали последний дефис в слове
            new_chant+= new_word + ' ' # добавили слово в строчку кричалки
        new_chant += '\n' # добавили новую строчку

    print()
    print(new_chant)
    return new_chant

# формат слога такой:
# xxox- , где х - согласная, о - гласная, тире это тире
def syllables_generator(letters):
    syllable = str()
    for i in range(len(letters)):
        if randint(0,100) <= percents[i]: syllable += letters[i]
    return syllable

def push_Vinnie_to_start():
    print(msg['intro'])
    while True:
        user_input = input(msg['choice'])
        chant = ''
        if user_input == '1': chant = chant_generator().split()
        elif user_input == '2': 
            chant = input(msg['user_chant']).split()
            print()
        else: 
            print(msg['bye'])
            break
        # print()
        print(msg['yes'] if ritm_checker(chant) else msg['no'])


msg = {'yes': 'Парам пам-пам (Винни - стихоплёт!)\n',
       'no': 'Пам парам (Сегодня Винни не в настроении..)\n',
       'intro': '\nСлогосчиталка кричалко-считалок от "Винни и Ко"\n',
       'choice': 'Жми 1, если хочешь проверить новую кричалку от Винни\nЖми 2, если хочешь проверить свою кричалку\nЛюбой другой ввод - потеряешь все акции "Винни и Ко": ',
       'user_chant': '\nпиши: ',
       'bye': 'Ты - банкрот!'}

percents = (80,30,100,40,90)
vowels = 'аеёиоуыэюя'
consonants = 'цйкнгшщзхфвпрлджчсмтб'
consonants_mini = 'трмпс' # а то совсем не читабельные кричалки

push_Vinnie_to_start()

#################################################################
#######---> ----------------------------------------- <---#######
####---->>> Подвал не законченных или не удачных идей <<<----####
#######---> ----------------------------------------- <---#######
#################################################################

# random.choices(['Катя', 'Коля'], weights=[10, 20])
# random.getrandbits(1) # 1-битовый возврат , только 1 или 0, как раз тру-фолс

def ritm_checker_1(word_list):
    ritms = list()
    for word in word_list:
        counter = 0
        for letter in word:
            if letter in vowels: counter+=1
        ritms.append(counter) 
        
        if len(ritms) == 1: continue
        if ritms[-1] != ritms[-2]:
            return False # что бы не проверять стишком из тысячи слов, если второе уже будет не в ритм. Э - экономия
    return True
    
def ritm_checker_2(word_list):
    vow1 = -1
    for word in word_list:
        vow2 = 0
        for letter in word:
            if letter in vowels: vow2+=1        
        if vow1 == -1: 
            vow1 = vow2
            continue
        if vow1 != vow2: 
            return False # что бы не проверять стишком из тысячи слов, если второе уже будет не в ритм. Э - экономия
        vow1 = vow2
    return True

def chant_generator_1():
    new_chant = str()
    for row in range(randint(1,4)):
        # current_vowel = choice(vowels)
        # current_consonants = [choice(consonants) for _ in range(3)] + ['-']
        # print(current_vowel, current_consonants)

        current_letters = [choice(consonants) for _ in range(3)] + ['-']
        current_letters.insert(2, choice(vowels))
        # print(current_letters)
        print()

        for word in range(randint(1,3)):
            for syllable in range(randint(1,4)):
                new_chant += syllables_generator(current_letters)
            new_chant = new_chant.rstrip('-')
            new_chant+= ' '
        new_chant += '\n'
    print(new_chant)
    return new_chant

# формат слога такой:
# xxox-
# х - согласная, о - гласная, тире это тире
# обязательна только гласная
def syllables_generator_1(letters):
    syllable = str()
    for i in letters:
        if i in vowels: syllable += i
        elif choice([True, False]): syllable += i
    # print(f'sylble is: {syllable}')
    return syllable





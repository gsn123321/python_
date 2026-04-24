import random
from rich.prompt import Prompt

def word():
    while True:
        try:
            word = input('Введіть слово для гри: ')
            
            if word.isdigit():
                raise Exception
                 
        except Exception:
            continue
        
        with open('word.txt', 'a', encoding='utf-8') as file:
            file.write(word + '\n')
        print('Слово записано')
        break

def draw_hangman(tries):
    stages = [
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    print(stages[tries])

def play():
    try:
        with open('word.txt', 'r', encoding='utf-8') as file:
            words = file.readlines()
    except:
        print('Пусто')
        return

    word = random.choice(words).strip()
    hidden = ['_'] * len(word)
    used_letters = []
    tries = 0
    max_tries = 6

    while tries < max_tries:
        print('Слово:', ' '.join(hidden))
        print('Використані букви:', ', '.join(used_letters))

        choice = input('Введіть букву або слово: ').lower()

        if len(choice) > 1:
            if choice == word:
                print('Ви виграли')
                history(True, word)
                return
            else:
                print('Неправильно')
                tries += 1

        else:
            if choice in used_letters:
                print('Ви вже вводили цю букву')
                continue

            used_letters.append(choice)

            if choice in word:
                for i in range(len(word)):
                    if word[i] == choice:
                        hidden[i] = choice
            else:
                print('Нема такої букви')
                tries += 1

        draw_hangman(tries)

        if '_' not in hidden:
            print('Ви програли, слово:', word)
            history(True, word)
            return

    print('Ви програли, cлово:', word)
    history(False, word)

def history(win, word):
    with open('stats.txt', 'a', encoding='utf-8') as file:
        if win:
            file.write(f'Перемога | слово: {word}\n')
        else:
            file.write(f'Поразка | слово: {word}\n')


def stats():
    try:
        with open('stats.txt', 'r', encoding='utf-8') as file:
            print('Історія ігор:')
            print(file.read())
    except:
        print('Історія пуста')

def menu():
    while True:
        print('[ 1 ] Почати гру')
        print('[ 2 ] Добавити слово')
        print('[ 3 ] Історія ігор')
        print('[ 4 ] Вихід')

        choice = Prompt.ask('Вибери дію: ', choices=['1', '2', '3', '4'])
        if choice == '1':
            play()
        elif choice == '2':
            word()
        elif choice == '3':
            stats()
        elif choice == '4':
            break
        
menu()
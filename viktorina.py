import random as r
from rich.prompt import Prompt

def word():
    while True:
        try:
            word = input('Введіть слово для гри: ')
            
            if word.isdigit():
                raise Exception
                 
        except Exception:
            continue
        
        word = list(word)
        with open('word.txt', 'a', encoding='utf-8') as file:
            file.write(word + '\n')
        print('Слово записано')
        break

def guess_letter():
    with open('word.txt', 'r', encoding='utf-8') as file:
        word = r.choice(file.readlines()).strip()

    hidden = ['_'] * len(word)

    player = input('Введіть букву: ')
    if player in word:
        for i in range(len(word)):
            if word[i] == player:
                hidden[i] = player
    else:
        print('Нема такоі букви') 

def guess_word():
    with open('word.txt', 'r', encoding='utf-8') as file:
        word = r.choice(file.readlines()).strip()
    
    player = input('Введіть слово: ')
    if player == word:
        print('Ти виграв')
    else:
        print('Ти програв')

def game():
    print('[ 1 ] Вгадати букву')
    print('[ 2 ] Вгадати слово')
    
    choice = Prompt.ask('Дія: ', choices=['1', '2'])

    if choice == '1':
        guess_letter()    

    elif choice == '2':
        guess_word()

def stats():
    print('')

def menu():
    while True:
        print('[ 1 ] Почати гру')
        print('[ 2 ] Добавити слово')
        print('[ 3 ] Історія ігор')
        print('[ 4 ] Вихід')

        choice = Prompt.ask('Вибери дію: ', choices=['1', '2', '3', '4'])
        if choice == '1':
            game()
        elif choice == '2':
            word()
        elif choice == '3':
            stats()
        elif choice == '4':
            break
        
menu()
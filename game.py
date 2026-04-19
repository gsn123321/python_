import random as r
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def player_choice():
    list = ['камень', 'ножницы', 'бумага']
    while True:
        choices = input('Выбери: камень или ножницы или бумага: ')
        if choices not in list:
            print('неверный выбор')
        else: 
            return choices   

def comp_choice():
    list = ['камень', 'ножницы', 'бумага']
    choices = r.choice(list)
    return choices

def game():
    raund = 0
    player = player_choice()
    random = comp_choice()
    print('Игрок', player)    
    print('Комп', random)

    try:
        with open('file.txt', 'r', encoding='utf-8') as f:
            raund = len(f.readlines()) + 1
    except FileNotFoundError:
        raund = 1
    
    if player == random:
        console.print('Ничья', style='yellow')
        raund +=1
        result = 'ничья'
    elif player == 'камень' and random == 'ножницы' or player == "ножницы" and random == "бумага" or player == "бумага" and random == "камень":
        console.print('Выйграл', style='green')
        raund+=1
        result = 'победа'
    else:
        console.print('Проиграл', style='red')
        raund+=1
        result = 'поражение'  
    save(result, player, random, raund)


def save(result, player, random,raund):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{player}, {random}, {result}, {raund}\n')         

def show():
    table = Table(title='Исторрия игр')

    table.add_column('Игрок', style='cyan')
    table.add_column('Комп', style='magenta')
    table.add_column('Результат', style='green')
    table.add_column('Раунд')

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            raund, player, random, result = line.split(", ") 
            table.add_row(raund, player, random, result)
    console.print(table)



while True:
        print('[ 1 ] Почати гру')
        print('[ 2 ] Історія ігор')
        print('[ 3 ] Статистика')
        print('[ 4 ] Вихід')

        choice = Prompt.ask("Выбери действие", choices=["1", "2", "3", "4"])
        if choice == '1':
            print('Начало игры')
            game()
        elif choice == '2':
            show()
        elif choice == '3':
            print('')
        elif choice == '4':
            break
            
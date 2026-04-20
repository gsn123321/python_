import random as r
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def player_choice():
    choices = Prompt.ask("Выбери действие", choices=["камень", "ножницы", "бумага"])
    return choices   

def comp_choice():
    ruka = ['камень', 'ножницы', 'бумага']
    choices = r.choice(ruka)
    return choices

raund = 1

def game():
    global raund
    player = player_choice()
    random = comp_choice()
    print('Игрок', player)    
    print('Комп', random)

    
    if player == random:
        console.print('Ничья', style='yellow')
        result = 'ничья'
    elif player == 'камень' and random == 'ножницы' or player == "ножницы" and random == "бумага" or player == "бумага" and random == "камень":
        console.print('Выйграл', style='green')
        result = 'победа'
    else:
        console.print('Проиграл', style='red')
        result = 'поражение'  
    save(result, player, random, raund)
    raund += 1

def stats():
    win = 0
    lose = 0
    draw = 0

    with open('file.txt', 'r', encoding='utf-8') as file:
        for line in file:
            result = line.strip().split(', ')[2]

            if result == 'победа':
                win += 1
            elif result == 'поражение':
                lose += 1
            elif result == 'ничья':
                draw += 1
    console.print(Panel(f'Победы: {win}, Поражения: {lose}, Ничьи: {draw}', title="Статистика", style='bold blue'))


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
            stats()
        elif choice == '4':
            break
            
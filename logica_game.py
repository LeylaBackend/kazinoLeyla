import random
from decouple import config

def play():
    slots = list(range(1,31))
    win = random.choice(slots)
    money = float(config("MY_MONEY"))
    playing = True
    while playing:
        print(f'Your balance {money}')
        bid = float(input('Bid: '))
        slot_selection = (int(input('Which slot will you put it on?(select from 1 to 30) ')))
        if slot_selection == win:
            money += 2 * bid
            print('YOU WIN!!!')
        else:
            money -= bid
            print('you lost...')
        skating_rink = input('Do you want play again? ')
        if skating_rink == 'No':
            playing = False
            print('Good bye')
        if skating_rink == 'Yes' and money <= 0:
            print('You have no funds')
            playing == False
        elif skating_rink == 'Yes' and money > 0:
            print(f'Your balance {money}')
            bid = float(input('Bid: '))
            slot_selection = (int(input('Which slot will you put it on? ')))
            if slot_selection == win:
                money += 2 * bid
                print('YOU WIN!!!')
            else:
                money -= bid
                print('you lost...')



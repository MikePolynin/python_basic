import random

from card_2 import Card2
from card_3 import Card3
from card_4 import Card4
from card_5 import Card5
from card_6 import Card6
from card_7 import Card7
from card_8 import Card8
from card_9 import Card9
from card_10 import Card10
from jack import Jack
from queen import Queen
from king import King
from ace import Ace


def start(cards):
    user_cards = [random.choices(cards)[0](0)]
    while True:
        new_card = random.choices(cards)[0](0)
        if new_card not in user_cards:
            user_cards.append(new_card)
            break
    return user_cards


def get_winner(user_hand, computer_hand):
    print('\nВаша рука: {}'.format(user_hand))
    print('Рука компьютера: {}'.format(computer_hand))
    if user_hand > 21 and computer_hand > 21:
        print('У всех перебор. Ничья')
    elif user_hand > 21 and computer_hand < 21:
        print('У вас перебор. Компьютер победил')
    elif user_hand < 21 and computer_hand > 21:
        print('У компьютера перебор. Вы победили')
    else:
        user_dif = 21 - user_hand
        computer_dif = 21 - computer_hand
        if computer_dif < user_dif:
            print('Компьютер победил')
        elif computer_dif > user_dif:
            print('Вы победили')
        else:
            print('Ничья')


class Blackjack:
    cards = [Card2, Card3, Card4, Card5, Card6, Card7, Card8, Card9, Card10, Jack, Queen, King, Ace]
    user_hand = 0
    computer_hand = 0
    user_cards = start(cards)
    computer_cards = start(cards)

    for card in user_cards:
        user_hand += card.coast

    for card in computer_cards:
        computer_hand += card.coast

    while True:
        print('\nВаша рука - {}'.format(user_hand))
        choice = input('1 - взять карту, 2 - завершить: ')
        if choice == '1':
            while True:
                new_card = random.choices(cards)[0](user_hand)
                if new_card not in user_cards:
                    user_cards.append(new_card)
                    user_hand += new_card.coast
                    break
        elif choice == '2':
            get_winner(user_hand, computer_hand)
            break
        else:
            print('Некорректный ввод')

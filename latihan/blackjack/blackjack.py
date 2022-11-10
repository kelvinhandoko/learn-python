import random
import card
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

user_cards = []
comp_cards = []
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King"]
SYMBOL = ["Diamonds", "Clubs", "Spades", "Hearts"]
is_game_over = False
clear = lambda: os.system("clear")


def deal_card():
    """fungsi ini gunanya untuk membagikan kartu secara acak
    kepada user maupun komputer."""
    index = random.randint(0, len(RANKS) - 1)
    rand_symbol = random.choice(SYMBOL)
    if index == 0:
        value = 11
    elif index > 8:
        value = 10
    else:
        value = index + 1
    result = {"card": card.ascii_version_of_card(card.Card(rand_symbol, RANKS[index])), "value": value}
    return result


def combineStr(*card):
    for lines in zip(*map(str.splitlines, card)):
        print(*(line.ljust(5) for line in lines))


def count_total(*value):
    hasil = 0
    for index, item in enumerate(value):
        if index > 0 and hasil >= 11 and item == 11:
            item = 1
        hasil += item
    return hasil


name = input("please enter your name : ")
comp_move_1 = deal_card()
comp_move_2 = deal_card()
comp_hidden_card = {"card": card.HIDDEN_CARD, "value": 0}
comp_cards.extend([comp_move_1, comp_move_2, comp_hidden_card])
user_move_1 = deal_card()
user_move_2 = deal_card()
user_cards.extend([user_move_1, user_move_2])
print("computer :")
combineStr(comp_cards[2]["card"], comp_cards[1]["card"])
print(f"{name} : ")
combineStr(user_cards[0]["card"], user_cards[1]["card"])
while not is_game_over:
    want_next_card = input("type 'y' to get another card, type 'n' to pass. ")
    clear()
    if want_next_card == "y":
        print("computer :")
        combineStr(comp_cards[2]["card"], comp_cards[1]["card"])
        print(f"{name} : ")
        user = deal_card()
        user_cards.append(user)
        user_card = [user["card"] for user in user_cards]
        combineStr(*user_card)
        user_card_value = [user["value"] for user in user_cards]
        comp_card_value = [comp["value"] for comp in comp_cards]
        user_total = count_total(*user_card_value)
        comp_total = count_total(*comp_card_value)
        print(user_total)
        if user_total > 21:
            clear()
            print(f"{name} : ")
            combineStr(*user_card)
            print(f"your card total is {user_total}. you lose!")
            break
    else:
        user_card_value = [user["value"] for user in user_cards]
        comp_card_value = [comp["value"] for comp in comp_cards]
        user_total = count_total(*user_card_value)
        comp_total = count_total(*comp_card_value)
        print("computer :")
        combineStr(comp_cards[0]["card"], comp_cards[1]["card"])
        print(f"{name} : ")
        user_card = [user["card"] for user in user_cards]
        combineStr(*user_card)
        if user_total == comp_total:
            print("the result is draw")
            break
        elif user_total > comp_total:
            if user_total == 21:
                print("you win (blackjack)")
                break
            else:
                print("you win")
                break
        else:
            print("you lose")
            break

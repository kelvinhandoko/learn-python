import os
from simple_chalk import chalk

clear = lambda: os.system("clear")
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(chalk.redBright(logo))
should_continue = True
bidder = []


def add_player(name: str, bid: int):
    bidder.append({"name": name, "bid": bid})


while should_continue:
    name = input("what is your name? ")
    bid = int(input("how much do you want to bid? $"))
    add_player(name, bid)
    add_another_player = input("do you have another player? type 'yes' or 'no' ")
    if add_another_player == "no":
        max_bid = max(i["bid"] for i in bidder)
        winner = list(filter(lambda x: x["bid"] == max_bid, bidder))[0]
        print(f"the winner is {name} and the bid is ${bid}".format(winner))
        should_continue = False
    else:
        clear()

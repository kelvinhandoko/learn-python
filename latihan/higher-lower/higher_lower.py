from data import data
from art import logo, vs
from random import choice


def random_data(data):
    return choice(data)


def check_higher(a, b):
    if a["follower_count"] < b["follower_count"]:
        return "a"
    else:
        return "b"


first = random_data(data)
second = random_data(data)

print(logo)
print(f"A. {first['name']} was {first['description']} from {first['country']}")
print(vs)
print(f"B. {second['name']} was {second['description']} from {second['country']} ")
user_input = input("who got more followers? type 'A' or 'B' ")
winner = check_higher(first, second)
if user_input.lower() == winner:
    print("you win")
else:
    print("you lose")

import os
import random
from unittest import result

logo = """                                       .__                                                     
   ____   __ __   ____    ______  ______|__|  ____     ____      ____  _____     _____    ____  
  / ___\ |  |  \_/ __ \  /  ___/ /  ___/|  | /    \   / ___\    / ___\ \__  \   /     \ _/ __ \ 
 / /_/  >|  |  /\  ___/  \___ \  \___ \ |  ||   |  \ / /_/  >  / /_/  > / __ \_|  Y Y  \\  ___/ 
 \___  / |____/  \___  >/____  >/____  >|__||___|  / \___  /   \___  / (____  /|__|_|  / \___  >
/_____/              \/      \/      \/          \/ /_____/   /_____/       \/       \/      \/ "
"""
is_going = True
clear = lambda: os.system("clear")
attempt = 10
RAND_NUMBER = random.randint(1, 100)


def compare(rand: int, user: int):
    global attempt
    if rand == user:
        condition = f"yeah the number is {RAND_NUMBER}"
    elif rand < user:
        condition = "too high"
        attempt -= 1
    else:
        condition = "too low"
        attempt -= 1
    return condition


print(logo)
print("welcome to guessing game")
print(f"your number is {RAND_NUMBER}")
print("i'm thinking number from 1 to 100")
level = input("choose difficulty. Type 'easy' or 'hard': ")
if level.lower() == "hard":
    attempt = 5
while is_going:
    print(f"your attempt {attempt} more")
    user_guess = int(input("enter the number: "))
    clear()
    result = compare(RAND_NUMBER, user_guess)
    print(result)
    if result == f"yeah the number is {RAND_NUMBER}":
        is_going = False
    if attempt < 1:
        print("you lose")
        is_going = False

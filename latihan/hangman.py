from random import choice
from word import word_list
from simple_chalk import chalk
import os

rand_word = choice(word_list)
rand_word_length = len(rand_word)
display = ["_" for i in range(rand_word_length)]
clear = lambda: os.system("clear")
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

logo = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """

end_of_game = False
count_wrong = 0
print(chalk.greenBright(logo))
while not end_of_game:
    print(f"\nlives : {6 - count_wrong}")
    print(chalk.red(stages[count_wrong]))
    user_guess = input("what letter do you guess? ").lower()
    print(user_guess)
    clear()
    if user_guess == "magic word":
        print(f"{rand_word} is the solution")
    if user_guess in display:
        print(f"you've already guessed {user_guess}")
    if user_guess not in rand_word and user_guess != "magic word":
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        count_wrong += 1
    else:
        print("next\n")
    index = [index for index, letter in enumerate(list(rand_word)) if letter == user_guess]
    for i in index:
        display[i] = user_guess
    print(" ".join(display))
    if count_wrong == 6:
        print("sorry your dead")
        end_of_game = True
    if "_" not in display:
        end_of_game = True
        print(f"yeah the word is {rand_word}")
        print("you win the game")

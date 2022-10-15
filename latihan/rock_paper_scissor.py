from random import randint, random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
all_choice = [rock, paper, scissors]
# Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_input > 2 or user_input < 0:
    print("invalide number!!! you lose")
else:
    user_choice = all_choice[user_input]
    comp_value = randint(0, len(all_choice) - 1)
    comp_choice = all_choice[comp_value]
    if user_input == comp_value:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER{comp_choice}")
        print("\tYOU DRAW")
    elif user_input - comp_value == -2:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER{comp_choice}")
        print("\tYOU WIN")
    elif user_input - comp_value == 2:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER{comp_choice}")
        print("\tYOU LOSE")
    elif user_input - comp_value == 1:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER{comp_choice}")
        print("\tYOU WIN")
    elif user_input - comp_value == -1:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER{comp_choice}")
        print("\tYOU LOSE")
    else:
        print(f"YOU{user_choice}\t VS \n\nCOMPUTER {comp_choice}")
        print("\tYOU LOSE")

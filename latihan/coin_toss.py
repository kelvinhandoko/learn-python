from random import random
print("selamat datang di tossing koin 1 milliar.")
user_choice = input("pilih head atau tail ? ")
if (user_choice == "head" or user_choice == "tail"):
    if (user_choice == "head"):
        choice = 1
    else:
        choice = 0
    random_choice = round(random())
    koin = "head" if random_choice == 1 else "tail"
    if (choice == random_choice):
        print(f"koinya {koin}. selamat kamu menang 1 milliar.")
    else:
        print(f"koinya {koin}. yahh kamu kurang beruntung.")
else:
    print("pilihannya cuman head dan tail bg.")

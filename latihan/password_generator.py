# password generator
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def createPassword(huruf: int, simbol: int, angka: int) -> str:
    letter = ""
    symbol = ""
    number = ""
    for i in range(0, huruf):
        letter += random.choice(letters)
    for i in range(0, simbol):
        symbol += random.choice(symbols)
    for i in range(0, angka):
        number += random.choice(numbers)
    password = letter + symbol + number
    return password


easyPass = createPassword(nr_letters, nr_symbols, nr_numbers)
print(easyPass)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
temp = createPassword(nr_letters, nr_symbols, nr_numbers)
harder_pass = ""
for i in range(0, len(temp)):
    harder_pass += random.choice(list(temp))
print(harder_pass)

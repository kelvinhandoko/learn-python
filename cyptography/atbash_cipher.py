import string
import os

alphabet = list(string.ascii_lowercase)

should_do = True

clear = lambda: os.system("clear")


def encypt(word):
    """encrypt dan decrypt dapat dilakukan dengan algo yang sama"""
    encypt_text = ""
    for char in word:
        if char == " ":
            new_letter = " "
        else:
            index = alphabet.index(char) + 1
            new_letter = alphabet[-index]
        encypt_text += new_letter
    return encypt_text


while should_do:
    clear()
    word = input("input word to encypt or decypt : ")
    result = encypt(word)
    print(f"your decrypt or encrypt word is {result}")
    restart = input("do you want to do it again ? type 'yes' to restart, type 'exit' to end process. ")
    if restart == "yes":
        should_do = True
    else:
        should_do = False
print("oke bye.")

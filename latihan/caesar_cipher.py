import string
from simple_chalk import chalk

logo = (
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""
    """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP"""
    """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)
alphabet = list(string.ascii_lowercase)

print(chalk.greenBright(logo))

should_do = True


def caesar_cipher(word, shift, direction):
    if direction == "encode":
        new_word = encrypt(word, shift)
        print(f"your encrypted word is {new_word}")
    else:
        new_word = decrypt(word, shift)
        print(f"your decrypted word is {new_word}")


def encrypt(word, shift):
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypt_word = ""
    for i in word:
        if i == " ":
            new_letter = " "
        else:
            index = alphabet.index(i)
            new_letter = new_alphabet[index]
        encrypt_word += new_letter
    return encrypt_word


def decrypt(word, shift):
    """masukan kata dan akan dishift sesuai dengan keinginan kita"""
    new_alphabet = alphabet[shift:] + alphabet[:shift]
    decrypted_word = ""
    for i in word:
        index = new_alphabet.index(i)
        decrypted_word += alphabet[index]
    return decrypted_word


while should_do:
    direction = input("type 'encode' to encrypt or 'decode' to decrypt: \n")
    word = input("type your message? ")
    shift = int(input("how much do you want to shifted? "))
    caesar_cipher(word, shift, direction)
    restart_state = input("type 'exit' to end process or type 'again' to encode or decode. ")
    if restart_state == "exit":
        should_do = False
    else:
        should_do = True
else:
    print("okay bye.")

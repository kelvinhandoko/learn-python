import os

polybius_square = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "k"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"],
    ["j"],
]

clear = lambda: os.system("clear")


def encypt(word):
    encypt_word = ""
    for char in word:
        if char == " ":
            encypt_word += " "
        for row in range(len(polybius_square)):
            for col in range(len(polybius_square[row])):
                if char == polybius_square[row][col]:
                    encypt_word += str(row + 1) + str(col + 1)
    return encypt_word


def decrypt(word: str):
    list_char = word.split(" ")
    slice_word = [["".join(list_char[j][i : i + 2]) for i in range(0, len(list_char[j]), 2)] for j in range(len(list_char))]
    decrypt_text = ""
    for char in slice_word:
        for count in range(len(char)):
            for row in range(len(polybius_square)):
                for col in range(len(polybius_square[row])):
                    if char[count] == "".join([str(row + 1), str(col + 1)]):
                        decrypt_text += polybius_square[row][col]
        decrypt_text += " "
    return decrypt_text.strip()


should_do = True

while should_do:
    state = input("type 'encrypt' to encrypt and 'decrypt' to decrypt. ")
    clear()
    if state == "encrypt" or state == "decrypt":
        word = input(f"please input {state}ed word : ")
        if state == "encrypt":
            result = encypt(word)
            print(f"your encrypted word is {result}.")
        else:
            result = decrypt(word)
            print(f"your decrypted word is {result}.")
        restart = input("type 'exit' to end process. type 'again' to restart. ")
        if restart != "exit":
            should_do = True
        else:
            should_do = False
    else:
        print("please type either encrypt or decrypt.")

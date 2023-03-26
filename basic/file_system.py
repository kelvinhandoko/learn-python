# untuk membuka file kita bisa menggunakan open.
file = open("../algorithm/file.txt")
# untuk membaca isi file kita menggunakan read
content = file.read()
file.close()


# untuk mempermudah dalam pembukaan file, kita bisa menggunakan keyword with

with open("./basic/file.txt", mode="w") as file:
    file.write("enter new text by ")

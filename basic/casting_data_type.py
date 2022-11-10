# merubah satu tipe data ke tipe data lain


data_int = 1
print("data integer : ", data_int, ", type : ", type(data_int))

# menjadi string
data_string = str(data_int)
print("data string : ", data_string, ", type : ", type(data_string))

# menjadi float
data_float = float(data_string)
print("data float : ", data_float, ", type : ", type(data_float))

# menjadi boolean
data_boolean = bool(data_float)  # nilai selain 0 akan true
print("data boolean : ", data_boolean, ", type : ", type(data_boolean))

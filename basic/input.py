# belajar mengambil input dari user

# data yg dimasukan selalu string 
data = input("silahkan di input: ")

print("data yg diinput adalah",data)
print("typenya adalah",type(data))

# jika ingin diinput dengan tipe data lain, boleh dicasting
data_float = float(input("silahkan diinput angka: "))

print("angka yg diinput adalah",data_float)
print("typenya adalah",type(data_float))

# jika ingin diinput dengan tipe data boolean
data_boolean = bool(int(input("silahkan diinput: ")))

print("data yg diinput adalah",data_boolean)
print("typenya adalah",type(data_boolean))



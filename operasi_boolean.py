# operasi boolean (not, or, and , xor)

# not (tidak)
print("====NOT====")
a = True
b = not a
print("not",a,"=",b)
a = False
b = not a
print("not",a,"=",b)

"""
or (jika data pertama adalah true maka dia akan mengambil nilai pertama, 
jika keduanya false maka akan mengambil nilai pertama juga) 
""" 
print("====or====")
a = False
b = True
c = a or b
print(a,"or",b,"=",c)
a = True
b = False
c = a or b
print(a,"or",b,"=",c)
a = False
b = False
c = a or b
print(a,"or",b,"=",c)
a = True
b = True
c = a or b
print(a,"or",b,"=",c)

"""
AND (jika data pertama adalah false maka dia akan false, 
pada AND kedua nilai harus TRUE) 
""" 
print("====and====")
a = False
b = True
c = a and b
print(a,"and",b,"=",c)
a = True
b = False
c = a and b
print(a,"and",b,"=",c)
a = False
b = False
c = a and b
print(a,"and",b,"=",c)
a = True
b = True
c = a and b
print(a,"and",b,"=",c)

"""
XOR (pada XOR nilai akan true jika salah satu nilainya true)
"""
print("====XOR====")
a = False
b = True
c = a ^ b
print(a,"^",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"^",b,"=",c)
a = False
b = False
c = a ^ b
print(a,"^",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"^",b,"=",c)

#latihan
print("====Latihan 1====")
user = int(input("masukan angka kurang dari 3\natau\nlebih dari 5 : "))

is_valid = user < 3 or user > 5
print("hasilnya",is_valid) 

print("====Latihan 2====")
user = int(input("masukan angka yang bisa dibagi 3 dan 8 : "))

is_valid = user % 3 == 0 and user % 8 == 0
print("hasilnya",is_valid) 
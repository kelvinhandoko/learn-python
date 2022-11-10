# bitwise (operasi binary)

a = 10
b = 8

# bitwise OR (|)
print("\n==== bitwise OR ====\n")
c = a | b
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai :",b, ", binary :",format(b,"08b"))
print("nilai",a,"|",b, ":",c ,"binary :",format(c,"08b"))

# bitwise and (&)
print("\n==== bitwise AND ====\n")
c = a & b
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai :",b, ", binary :",format(b,"08b"))
print("nilai",a,"&",b, ":",c ,"binary :",format(c,"08b"))

# bitwise XOR (^)
print("\n==== bitwise AND ====\n")
c = a ^ b
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai :",b, ", binary :",format(b,"08b"))
print("nilai",a,"^",b, ":",c ,"binary :",format(c,"08b"))

# bitwise NOT (~) disini nilainya akan minus
print("\n==== bitwise not ====\n")
c = ~a
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai","~"+str(a), ":",c ,"binary :",format(c,"08b"))

# shift right (>>)
print("\n==== bitwise shift right ====\n")
berapa_kali = 1
c = a >> berapa_kali
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai",a,">>",berapa_kali,":",c ,"binary :",format(c,"08b"))

# shift left (<<)
print("\n==== bitwise shift left ====\n")
berapa_kali = 2
c = a << berapa_kali
print("nilai :",a, ", binary :",format(a,"08b"))
print("nilai",a,"<<",berapa_kali,":",c ,"binary :",format(c,"08b"))



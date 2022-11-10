# contoh operasi komparasi ( <, >, <=, >=,==, !=, is, is not), tipe data hasil komparasi selalu boolean

a = 10
b = 8

# lebih besar dari ( > )
hasil = a > b

print(a,">",b,"=",hasil)

# lebih kecil dari ( > )
hasil = a < 11

print(a,"<",11,"=",hasil)

# lebih besar dengan ( >= )
hasil = a <= a

print(a,">=",a,"=",hasil)

# lebih kecil sama dengan ( <= )
hasil = a <= 10

print(a,"<=",10,"=",hasil)

# sama dengan ( == )
hasil = a == 10

print(a,"==",10,"=",hasil)

# tidak sama dengan ( != )
hasil = a != 10

print(a,"!=",10,"=",hasil)

# is untuk komparasi object identity
x = 5
y = 5

print("nilai x =",x,"dan idnya =",hex(id(x)))
print("nilai y =",y,"dan idnya =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

# is not untuk komparasi kedua object identity tidak sama
y = 10

print("nilai x =",x,"dan idnya =",hex(id(x)))
print("nilai y =",y,"dan idnya =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)
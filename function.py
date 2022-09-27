# fungsi
from re import S


def tambah_Angka(*args:int) -> int:
    hasil = 0
    for angka in args:
        hasil += angka
    
    print(hasil)

tambah_Angka(2,1,3,4,10)
print("\n")
def fizz_buzz(jumlah:int)->None:
    for number in range(1,jumlah + 1):
        if(number % 3 == 0):
            print("fizz")
        elif(number % 5 == 0):
            print("buzz")
        elif(number % 15 == 0):
            print("fizzBuzz")
        else:
            print(number)

fizz_buzz(20)
print("\n")

# lambda

kali_2 = lambda angka:angka * 2
print(kali_2(3))

pangkat = lambda angka,power:angka ** power
print(pangkat(3,2))

data = ['anjay','apaantu',"boss"]
data.sort(key=lambda data:len(data))
print(data)
data_angka = list(range(0,21))
data_baru = list(filter(lambda x:x %2 == 0,data_angka))
print(data_baru)

# anonymous function
def pangkat(n:int):
    return lambda angka:angka ** n
pangkat_3 = pangkat(3)
print(pangkat_3(20))

angka = 3.123421    
print(f"{angka:.4f}")
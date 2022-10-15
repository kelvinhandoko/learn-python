from math import isqrt
#cek apakah angka tersebut merupakan perfect squares
angka = int(input("masukan angka yang mau di cek : "))
hasil = isqrt(angka)

if(hasil ** 2 == angka):
    print(f"{angka} merupakan perfect squares dan merupakan pangkat dari {hasil}")
else:
    print(f"{angka} bukan merupakan perfect square")

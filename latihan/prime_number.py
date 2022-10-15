
# menentukan angka tersebut merupakan prima atau tidak
from math import isqrt

angka = int(input("masukan angka yang mau di check : "))

if (angka > 1):
    for i in range(2, isqrt(angka) + 1):
        if (angka % i == 0):
            print(f"{angka} bukan bilangan prima")
            break
    else:
        print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")

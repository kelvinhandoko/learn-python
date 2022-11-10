# contoh perhitungan sederhana
from math import sqrt


a = 20
b = 2
c = 16

tambah = a + b
kurang = a - b
kali = a * b
bagi = a / b # pembagian otomatis data typenya float
pangkat = a ** b
akar = sqrt(c)
modulus = a % c
floor_division = a // c # pembulatan pembagian dibulatkan kebawah

print("hasil",a, "+",b ,"adalah",tambah)
print("hasil",a, "-",b ,"adalah",kurang)
print("hasil",a, "*",b ,"adalah",kali)
print("hasil",a, "/",b ,"adalah",bagi)
print("hasil",a, "**",b ,"adalah",pangkat)
print("hasil akar",c, "adalah",akar)
print("hasil",a, "mod",c ,"adalah",modulus)
print("hasil",a, "//",c ,"adalah",floor_division)

# latihan conversi temperature
print("\n===LATIHAN CONVERSI TEMPERATURE DARI CELCIUS===\n")
celcius = float(input("berapa suhunya dalam celcius : "))
fahrenheit = round(celcius * (9/5)+ 32,2)
reamur = round(celcius * (4/5),2)
kelvin = celcius + 273

print("suhu dalam celcius :",celcius)
print("suhu dalam fahrenheit :",fahrenheit)
print("suhu dalam reamur :",reamur)
print("suhu dalam kelvin :",kelvin)
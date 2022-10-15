# menentukan apakah 3 angka merupakan triple pythagoras.

angka = input("masukan 3 angka : ")
number = [int(x) for x in angka.split(" ")]
number.sort()
if(number[0]**2 + number[1]**2 == number[2]**2):
    print(f"{number[0]},{number[1]},{number[2]} merupakan triple pythagoras")
else:
    print(f"{number[0]},{number[1]},{number[2]} bukan merupakan triple pythagoras")
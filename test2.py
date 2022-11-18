# masukan = input("masukan angka :")
# angka_list = [int(angka) for angka in masukan.split()]

# ganjil = 0
# genap = 0

# for i in angka_list:
#     if i % 2 == 0:
#         genap += 1
#     else:
#         ganjil += 1

# print(ganjil)
# print(genap)


n = int(input("masukan jumlah angka yang mau dicek : "))
ganjil = 0
genap = 0
for i in range(n):
    angka = int(input(f"masukan angka ke-{i+1} "))
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1
print(f"ganjil:{ganjil}")
print(f"genap:{genap}")

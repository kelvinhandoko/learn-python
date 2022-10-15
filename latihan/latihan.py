
# no 2
jam_masuk = int(input("masukan jam masuk : "))
jam_keluar = int(input("masukan jam keluar : "))

selisih = jam_keluar - jam_masuk
if(jam_masuk < 1 or jam_masuk > 24):
    print("masukan jam masuk dari 1 - 24")
elif(jam_keluar < 1 or jam_keluar > 24 ):
    print("masukan jam keluar dari 1 - 24")
elif( selisih < 0 ):
    print("jam keluar harus lebih besar dari jam masuk")
else :     
    if(selisih > 2):
        hasil = 4000 + (selisih - 2) * 500
    else:
        hasil = selisih * 2000
    print(f"biaya parkir selama {selisih} jam adalah {hasil}")

# no 3
hari = input("masukan hari : ")
total_pesanan = int(input("masukan total pesanan anda : "))

valid_day = ["jumat","sabtu","minggu"]
if(hari in valid_day and total_pesanan >= 40000):
    diskon = int(total_pesanan * 40/100)
    if(diskon > 50000):
        diskon = 50000
    print(f"anda bisa menggunakan voucher dengan total diskon {diskon}")
else:
    print(f"voucher tidak bisa dipakai di hari {hari}")
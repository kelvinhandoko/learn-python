# integer
from re import A


print("\n==== INTEGER ==== \n")
integer = 10
print("data integer:",integer,", bertipe : ",type(integer))

# float (decimal)
print("\n==== FLOAT ==== \n")
float = 1.52
print("data float:",float,", bertipe : ",type(float))

# string (karakter)
print("\n==== STRING ==== \n")
string = "ini contoh string"
print("data string:",string,", bertipe : ",type(string),"\n")
# operasi dan manipulasi string
print("-operasi string")
#- concat(menyambungkan)
print("1.concat")
nama_depan = "apa"
nama_belakang = "anjay"
nama_lengkap  = nama_depan + " " + nama_belakang
print("nama depan :",nama_depan)
print("nama belakang :",nama_belakang)
print("nama lengkap :",nama_lengkap)

#- length (len)
print("\n2.length (len)")
length = len(nama_lengkap)
print("panjang string nama lengkap :",length)

#- mengecek ada tidaknya huruf pada suatu string
print("\n3.mengecek ada tidaknya huruf")
huruf = "s"
valid = huruf in nama_lengkap
print("apakah huruf",huruf,"ada di,",nama_lengkap,":",valid)

#- repeat string
print("\n4.repeat string")
repeat = "apa"*10
print(repeat)

#- indexing
print("\n5.indexing")
index = 5
print('index ke',index,"dari",nama_lengkap,"adalah",nama_lengkap[index])
# jika ingin langsung index terakhir bisa pake -1 dan seterusnya
print('index terakhir dari',nama_lengkap,"adalah",nama_lengkap[-1])
print('index kedua terakhir dari',nama_lengkap,"adalah",nama_lengkap[-2])
# indexing juga bisa dengan range ([dari:sampai - 1:increment])
print("index [1:3] dari",nama_lengkap,"adalah",nama_lengkap[0:10:2])

print("\n-method pada string")
# count
index = 1
print(str(index)+".","count")
kata = "apakabardunia"
huruf = "a"
hasil = kata.count("a")
print("jumlah",huruf,"pada",kata,"adalah",hasil)


# boolean (true or false)
print("\n==== BOOLEAN ==== \n")
boolean = False
print("data boolean:",boolean,", bertipe : ",type(boolean))

# bilangan complex
print("\n==== COMPLEX ==== \n")
bil_complex = complex(5,1)
print("data bil_complex:",bil_complex,", bertipe : ",type(bil_complex))

# tipe data dari C (harus diimport dulu!)
print("\n==== OTHER ==== \n")
from ctypes import c_double

data_c_double = c_double(10.3)
print("data c_double:",data_c_double ,", bertipe : ",type(data_c_double ))


# integer
integer = 10
print("data integer:",integer,", bertipe : ",type(integer))

# float (decimal)
float = 1.52
print("data float:",float,", bertipe : ",type(float))

# string (karakter)
string = "ini contoh string"
print("data string:",string,", bertipe : ",type(string))

# boolean (true or false)
boolean = False
print("data boolean:",boolean,", bertipe : ",type(boolean))

# bilangan complex
bil_complex = complex(5,1)
print("data bil_complex:",bil_complex,", bertipe : ",type(bil_complex))

# tipe data dari C (harus diimport dulu!)
from ctypes import c_double

data_c_double = c_double(10.3)
print("data c_double:",data_c_double ,", bertipe : ",type(data_c_double ))


# testing standart library
import datetime as date
from collections import Counter

hari_ini = date.datetime.now().strftime("%A")
print(f"Today is {hari_ini}")

data = ["a","a","c","c","f"]
count_data = Counter(data)
for key,value in count_data.items():
    print(f"jumlah {key} : {value}")

a = 10
print(f"{a:b}")
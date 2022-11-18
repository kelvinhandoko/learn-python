# list atau array

list_1 = [1, 2, 3, 4]
print(list_1)

list_2 = list(range(0, 21, 2))  # range(start,stop - 1 , step(kalo minus brarti decrement))
print(list_2)

list_3_for = [i**2 for i in range(0, 11)]
print(list_3_for)

list_3_if = [i**2 for i in range(0, 11) if i % 2 != 0]
print(list_3_if)

# method di list
print("\n==== METHOD DI LIST ====\n")

# length (len)
print("LEN")
data = [1, 2, 3, 4]
print(f"datanya : {data}")
print(f"panjang datanya adalah {len(data)}")

# insert
print("\nINSERT")
item_baru = 5
print(f"item barunya : {item_baru}")
data.insert(0, item_baru)
print(f"datanya menjadi {data}")

# append
print("\nAPPEND")
item_baru = 6
print(f"item barunya : {item_baru}")
data.append(item_baru)
print(f"datanya menjadi {data}")

# extend
print("\n EXTEND")
list_baru = [2, 3, 4, 5]
print(f"list baru : {list_baru}")
data.extend(list_baru)
print(f"datanya menjadi {data}")

# REMOVE
print("\nREMOVE")
data_remove = 2
print(f"remove data : {data_remove}")
data.remove(data_remove)
print(f"datanya menjadi {data}")

# pop
print("\nPOP")
data.pop()
print(f"datanya menjadi {data}")

# count
print("\nCOUNT")
jumlah_data_1 = data.count(1)
print(f"jumlah angka 1 pada data adalah {jumlah_data_1}")

# sort
print("\nSORT")
data.sort()
print(f"data setelah di sort yaitu {data}")


# looping di list
print("\n==== LOOPING DI LIST ====")

# metode 1
for i in data:
    print(f"datanya : {i}")

# metode 2
[print(f"\ndata ke {index} : {i}") for index, i in enumerate(data)]


s = "sapi"
reveredString = "".join(list(s)[::-1])
print(reveredString)


# matriks1 = [[0 for _ in range(col)] for _ in range(baris)]
arr = []
for i in range(2):
    arr.append([])
for row in arr:
    for j in range(2):
        row.append(0)


print(arr)

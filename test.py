from math import factorial

n = int(input("n : "))
# diamond pattern
# for i in range(1, n + 1):
#     print(((i * 2 - 1) * "*").rjust(n + i))
# for i in range(n - 1, 0, -1):
#     print(((i * 2 - 1) * "*").rjust(n + i))

# inverted pyramid number
# for i in range(n, 0, -1):
#     print((str(n + 1 - i) + " ") * i)

# right-angled triangle pattern
# hasil = ""
# for i in range(1, n + 1):
#     hasil += " " + str(i)
#     print(hasil.rjust(n * 2))

# pascal tringle
# for i in range(n):
#     for j in range(n - i + 1):
#         print(end=" ")
#     for j in range(i + 1):
#         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
#     print()

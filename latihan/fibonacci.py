from re import A


# def fibo(n: int) -> int:
#     """
#     n adalah suku ke-n dari fibonacci
#     """
#     if n <= 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)


def fibo(n: int) -> int:
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


print(fibo(9))

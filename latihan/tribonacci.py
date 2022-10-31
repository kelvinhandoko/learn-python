def tribo(n):
    a = b = 0
    c = 1
    if n > 0:
        if n <= 2:
            return a
        elif n <= 4:
            return c
        else:
            for i in range(3, n):
                d = a + b + c
                a = b
                b = c
                c = d
            return c
    else:
        print("n must be positive integer")


print(tribo(20))

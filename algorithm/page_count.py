def pageCount(n, p):
    # Write your code here
    # n = max page
    # p = target
    # hal 1 = 0
    # hal trakhir = 0
    # hal 2-3 = 1
    # hal 1 -2 sebelum akhir = 1
    if n % 2 == 0:
        return int(min(p / 2, (n - p + 1) / 2))
    else:
        return int(min(p / 2, (n - p) / 2))


print(pageCount(6, 2))

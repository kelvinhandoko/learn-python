import math


def solution(n):
    sisa = n - 2 ** int(math.log2(n))
    print(sisa)
    if (sisa // 2) % 2 != 0 or n == 1:
        return "Ricahar"
    else:
        return "Louis"


print(solution(1560834904))

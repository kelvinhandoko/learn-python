def find_factor(n, banyak=2):
    count = 0
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            answer.append(i)
        if count == banyak:
            break
    if count < banyak:
        return f"angka {n} hanya memiliki {count} faktor yaitu {answer} "
    return answer


print(find_factor(100, 10))

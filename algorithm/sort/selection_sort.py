import random

num_arr = [random.randrange(1, 20) for _ in range(100)]


def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]


def smallest(arr, start, end):
    i = start
    j = i
    while i <= end:
        if arr[i] < arr[j]:
            j = i
        i += 1
    return j


def selection_sort(arr, size):
    i = 0
    while i < size - 1:
        j = smallest(arr, i, size - 1)
        swap(arr, i, j)
        i += 1


selection_sort(num_arr, len(num_arr))
print(num_arr)

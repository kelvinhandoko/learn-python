def solution(arr: list):
    mid_index = len(arr) // 2
    last = arr[mid_index + 1 : :]
    first = arr[:mid_index][::-1]
    return [*last, mid_index, *first]


print(solution([2, 3, 5, 1, 4]))

import random

num_arr = [random.randrange(1, 20) for _ in range(10000)]
# time complexity : O(n^2)
for i in range(len(num_arr)):
    for j in range(i):
        if num_arr[i] < num_arr[j]:
            num_arr[i], num_arr[j] = num_arr[j], num_arr[i]

print(num_arr)

"""
heap
left child : i * 2
right child : i * 1 + 1
parent : i / 2
"""

import heapq

data = [2, 3, 1, 4, 29, 10, 7, 100]
heapq.heapify(data)
heapq._heapify_max(data)
heapq.heappop(data)
print(data)

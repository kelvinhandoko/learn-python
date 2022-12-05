# queue -> FIFO
from collections import deque

price = []

# insert -> memasukan element
price.insert(0, 1000)
price.insert(0, 3000)

# pop -> mengeluarkan element
price.pop()
print(price)

# deque -> cara lain untuk queue
q = deque()
q.append(100)
print(list(q))

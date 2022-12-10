ar = [1, 1, 2, 3, 2, 4]
uniqueItem = []
[uniqueItem.append(item) for item in ar if item not in uniqueItem]
print(uniqueItem)

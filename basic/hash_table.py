class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for _ in range(self.MAX)]

    def hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


table = HashTable()
table["march 1"] = "opwwe"
table["march 6"] = "dribble"
table["march 3"] = 300
table["march 17"] = 132
table["march 5"] = 231
del table["march 17"]
print(table["march 6"])
print(table.arr)

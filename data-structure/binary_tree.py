import math


class Node:
    def __init__(self, val) -> None:
        self.right = None
        self.left = None
        self.val = val

    def printTree(self):
        pass

    def depth_first_values(self):
        stack = [self]
        while len(stack) > 0:
            cur = stack.pop()
            print(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

    def breadth_first_values(self):
        queue = [self]
        while len(queue) > 0:
            cur = queue.pop()
            print(cur.val)
            if cur.left:
                queue.insert(0, cur.left)
            if cur.right:
                queue.insert(0, cur.right)

    def tree_includes(self, target):
        stack = [self]
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val == target:
                return True
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return False

    def tree_sum(self):
        stack = [self]
        total = 0
        while len(stack) > 0:
            cur = stack.pop()
            total += cur.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        print(total)

    def tree_min_value(self):
        stack = [self]
        smallest = float("inf")
        while len(stack) > 0:
            cur = stack.pop()
            if cur.val < smallest:
                smallest = cur.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return smallest


def max_path_sum(root):
    if root == None:
        return float("-inf")
    if root.right == None and root.left == None:
        return root.val
    max_child = max(max_path_sum(root.left), max_path_sum(root.right))
    return root.val + max_child


a = Node(10)
b = Node(20)
c = Node(32)
d = Node(100)
e = Node(70)
f = Node(123)
g = Node(1200)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = g

print("depth first transversal\n")
a.depth_first_values()
print("\nbreath first transversal\n")
a.breadth_first_values()
print(a.tree_includes("b"))
a.tree_sum()
print(a.tree_min_value())
print(max_path_sum(a))

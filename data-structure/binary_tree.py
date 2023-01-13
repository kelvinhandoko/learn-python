import math


class Node:
    def __init__(self, val) -> None:
        self.right = None
        self.left = None
        self.val = val

    def printTree(self):
        queue = [self]
        new = []
        while len(queue) > 0:
            cur = queue.pop()
            new.append(cur.val)
            if cur.left:
                queue.insert(0, cur.left)
            if cur.right:
                queue.insert(0, cur.right)
        print(new)
        tingkatan = math.ceil(math.log2(len(new))) + 1

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
            if cur.right:
                queue.insert(0, cur.right)
            if cur.left:
                queue.insert(0, cur.left)

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


def in_order_transversal(root):
    if root:
        in_order_transversal(root.left)
        print(root.val, end=",")
        in_order_transversal(root.right)


def pre_order_transversal(root):
    if root:
        print(root.val, end=",")
        in_order_transversal(root.left)
        in_order_transversal(root.right)


def post_order_transversal(root):
    if root:
        post_order_transversal(root.left)
        post_order_transversal(root.right)
        print(root.val, end=",")


a = Node(2)
b = Node(7)
c = Node(5)
d = Node(2)
e = Node(6)
f = Node(9)
g = Node(5)
h = Node(11)
i = Node(4)
a.left = b
a.right = c
c.right = f
f.left = i
b.left = d
b.right = e
e.left = g
e.right = h
# c.right = g
# d.left = h
# d.right = i
# e.left = j
# print("depth first transversal\n")
# # a.depth_first_values()
print("\nbreath first transversal\n")
a.breadth_first_values()
# # print(a.tree_includes("b"))
# # a.tree_sum()
# # print(a.tree_min_value())
# # print(max_path_sum(a))
# a.printTree()
print("in-order")
in_order_transversal(a)
print("pre-order")
pre_order_transversal(a)
print("post-order")
post_order_transversal(a)

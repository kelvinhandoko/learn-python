class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LL is empty")
            return
        iterator = self.head
        ll_node = ""

        while iterator:
            if iterator.next == None:
                ll_node += str(iterator.data)
                iterator = iterator.next
            else:
                ll_node += str(iterator.data) + "-->"
                iterator = iterator.next
        print(ll_node)

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def append_list(self, list: list):
        for data in list:
            self.append(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count

    def remove(self, index: int):
        if index < 0 or index > self.get_length():
            raise IndexError("out of range")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("out of range")
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data=data, next=itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data=data_to_insert, next=self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data=data_to_insert, next=itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            itr = self.head
            while itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(200)
    ll.insert_at_beginning(200)
    ll.append(90)
    ll.append(90)
    # ll.append_list([200, 123, 200])
    # ll.remove(1)
    # ll.insert_at(5, 921)
    # ll.insert_at(0, 89)
    # ll.insert_after_value(200, 99)
    # ll.remove_by_value(200)
    ll.print()
    # ll.get_length()

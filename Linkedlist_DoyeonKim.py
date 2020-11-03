
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    # case 1
    # a->None,
    # a.insertNext (b)
    # a-> b

    # case 2
    # initial state: a -> c
    # a.insert (b) : a -> b ->
    # a -> b -> c

    def insert(self, right):
        if self.next == None:
            self.next = right

        else:
            temp = self.next
            self.next = right
            right.next = temp


a = Node(10)
b = Node(7)
c = Node (3)
a.insert(c)
a.insert(b)
print("finish")
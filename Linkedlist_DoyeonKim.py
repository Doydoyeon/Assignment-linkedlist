
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    # case 1
    # a->None,
    # a.insertNext (b)
    # a-> b

    # case 2
    # a -> c
    # a -> b -> c

    def insert(self, right):
        if self.next == None:
            self.next = right

        # else:
        #     if

a = Node(10)
b = Node(7)
a.insert(b)
print("finish")
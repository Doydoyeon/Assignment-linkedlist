
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

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_head):

        if self.head == None:
            self.head = new_head

        else:
            # written by doy
            temp = self.head
            self.head = new_head
            new_head.insert(temp)
            # self.head.insert(temp)

            # solution
            # new_head.insert(self.head)
            # self.head = new_head


    # IS:  self.head == a -> b-> c
    # insert (d): self.head == d -> a  (previous self.head)->b->c

a = Node(10)
b = Node(7)
c = Node(3)
d = Node(5)

linked_list = LinkedList()
linked_list.push(a)
linked_list.push(d)
linked_list.push(b)
linked_list.push(c)

print("finish")


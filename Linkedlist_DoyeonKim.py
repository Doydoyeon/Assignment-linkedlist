import numpy as np
import time

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

# setting some number with the variable n1, n2

n1 = 10000
n2 = 1000000

#
linkedlist_1 = LinkedList()
linkedlist_2 = LinkedList()

# create n1 nodes
for i in range(n1):
    node = Node(1)
    linkedlist_1.push(node)

# create n2 nodes
for i in range(n2):
    node = Node(1)
    linkedlist_2.push(node)


start = time.time()
tmpNode = Node(1)
linkedlist_1.push(tmpNode)
elapse1 = time.time() - start

start = time.time()
tmpNode = Node(1)
linkedlist_2.push(tmpNode)
elapse2 = time.time() - start

print ( elapse1 * 1000, elapse2*1000 )
print("finish")


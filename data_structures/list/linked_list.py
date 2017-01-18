
"""
+ :
 * easy insert/delete
 * no need to set start length
 * could grow/srink while runtime
- :
 * time to index
 * additional memory
 * hard to move backward
Tradeoffs:
 access: O(n)
 insert/delete first: O(1)
 insert/delete last:  O(1) / O(n)
 insert/delete middle: search + O(1)
 space: O(n)
"""
class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    while node:
        print(node)
        node = node.next

def print_backward(node):
    if node == None : return
    head = node
    tail = node.next
    print_backward(tail)
    print(head)

def add_after(node, new):
    new.next = node.next
    node.next = new

def add(list, new):
    head = list
    while head.next : head = head.next
    head.next = new

def remove_next(node):
    if node.next == None : return
    node.next = node.next.next
        
list = Node("1")

add(list, Node(0))
remove_next(list)
print_list(list)

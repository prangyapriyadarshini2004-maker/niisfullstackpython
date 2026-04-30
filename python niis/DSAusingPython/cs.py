# Linked List Create and Display using OOP Concept
class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None
class CLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        ch = True
        c = 1
        ptr = None
        while ch==1:
            c = c + 1
            print("Enter node", c, "data")
            ele = int(input())
            cur = Node(ele)
            cur.next=cur
            if self.head == None:
                self.head = cur
            else:
                ptr.next = cur
                cur.next=self.head
            ptr = cur
            print("Do you continue? Press 1")
            ch =int(input())
    def display(self):
        print("Elements are")
        ptr = self.head
        while ptr != self.head:
            print(ptr.data)
            ptr = ptr.next
        print(ptr.data)
obj =CLinkedList()
obj.create()
obj.display()
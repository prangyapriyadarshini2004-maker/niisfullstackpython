# Linked List Create and Display using OOP Concept

class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        ptr = None
        c = 1

        while True:
            ele = int(input(f"Enter node {c} data: "))
            cur = Node(ele)

            if self.head is None:
                self.head = cur
            else:
                ptr.next = cur

            ptr = cur
            c += 1

            ch = input("Do you want to continue? (y/n): ")
            if ch.lower() != 'y':
                break

    def display(self):
        ptr = self.head
        if ptr is None:
            print("List is empty")
            return

        print("Elements are:")
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("None")

    def insertend(self, data):
        cur = Node(data)

        if self.head is None:
            self.head = cur
            return

        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = cur
        print(f"{data} inserted at end")
obj = LinkedList()
obj.create()

print("\nBefore insertion:")
obj.display()

obj.insertend(5)

print("\nAfter insertion:")
obj.display()
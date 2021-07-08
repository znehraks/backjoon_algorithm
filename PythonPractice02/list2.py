class SinglyLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.cnt = 0

    def insert_head(self, value):
        node = self.Node(value)
        self.cnt += 1
        if not self.tail:
            self.tail = node
        node.next = self.head
        self.head = node

    def insert_tail(self, value):
        node = self.Node(value)
        self.cnt += 1
        if not self.head:
            self.head = node
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = node

    def delete_head(self):
        if not self.head:
            return
        self.cnt -= 1
        self.head = self.head.next

    def delete_tail(self):
        if not self.head:
            return
        p = self.head
        while p.next:
            p = p.next
            if not p.next.next:
                p.next = None
        self.cnt -= 1
        return

    def count(self):
        print(self.cnt)

    def print_all(self):
        if not self.head:
            return
        p = self.head
        while p:
            print(p.value, end=" ")
            p = p.next
        return

list = SinglyLinkedList()
list.insert_head('A')
list.insert_head('B')
list.insert_head('C')
list.insert_head('D')
list.insert_head('E')
list.insert_tail('F')
list.insert_tail('G')
list.delete_head()
list.delete_tail()
list.print_all()
list.count()

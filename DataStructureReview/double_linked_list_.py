class Linked_list:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

        def __str__(self):
            return f"NODE[{self.value}]"

    def __init__(self):
        self.head = self.Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        if self.head == self.head.next:
            return True
        return False

    def add_after(self, node, value):
        new = self.Node(value)
        new.next = node.next
        node.next.prev = new
        node.next = new
        new.prev = node

    def add_before(self, node, value):
        new = self.Node(value)
        new.next = node
        node.prev.next = new
        new.prev = node.prev
        node.prev = new

    def add_head(self, value):
        new_head = self.Node(value)
        new_head.next = self.head.next
        self.head.next.prev = new_head
        self.head.next = new_head
        new_head.prev = self.head

    def add_tail(self, value):
        new_tail = self.Node(value)
        new_tail.prev = self.head.prev
        self.head.prev.next = new_tail
        new_tail.next = self.head
        self.head.prev = new_tail

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_head(self):
        if self.is_empty():
            return
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def remove_tail(self):
        if self.is_empty():
            return
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev

    def traverse(self, dir=1):
        # generator를 이용하여 리스트를 정방향(dir=1) 혹은 역방향(dir=-1)으로 순회할 수 있도록 함
        node = self.head.next if dir == 1 else self.head.prev
        while node != self.head:
            yield node
            node = node.next if dir == 1 else node.prev

    def find(self, value, from_node=None):
        # from_node 다음부터 시작해서 value 값을 갖는 첫 노드를 찾아서 반환
        # 끝까지 찾아도 없으면 None을 반환
        if from_node == None:
            from_node = self.head
        node = from_node.next
        while node != self.head:
            if node.value == value:
                return node
            node = node.next
        return None

    def print(self, dir=1):
        # traverse를 이용하여 리스트를 프린트
        print("FORWARD: " if dir == 1 else "BACKWARD:", end="")
        for node in self.traverse(dir):
            print(node.value, end="->")
        print()


"""
FORWARD:
BACKWARD:
IS_EMPTY? True
FORWARD: 3->1->3->4->
BACKWARD: 4->3->1->3->
IS_EMPTY? False
NODE[3]
NODE[3]
FORWARD: 3->1->9->3->5->4->
BACKWARD: 4->5->3->9->1->3->
FORWARD: 3->1->9->3->5->
BACKWARD: 5->3->9->1->3->
FORWARD: 9->3->5->
BACKWARD: 5->3->9->
FORWARD: 9->
BACKWARD: 9->
IS_EMPTY? False
FORWARD:
IS_EMPTY? True
"""
if __name__ == "__main__":
    list = Linked_list()
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    list.add_head(1)
    list.add_head(3)
    list.add_tail(3)
    list.add_tail(4)
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    a = list.find(3)
    print(a)
    b = list.find(3, from_node=a)
    print(b)
    list.add_before(b, 9)
    list.add_after(b, 5)

    list.print()
    list.print(-1)

    c = list.find(4)
    list.remove(c)

    list.print()
    list.print(-1)

    list.remove_head()
    list.remove_head()

    list.print()
    list.print(-1)

    list.remove_tail()
    list.remove_tail()

    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    list.remove_head()
    list.print()
    print("IS_EMPTY?", list.is_empty())

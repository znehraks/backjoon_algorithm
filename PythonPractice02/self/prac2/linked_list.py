"""
아래에 학번과 이름을 꼭 적으세요.

학번:60152572   
이름:유정민
"""


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            # 받은 value를 self.value에 저장
            self.next = None
            # 받은 next를 self.value에 저장
            self.prev = None
            # 받은 value를 self.value에 저장

        def __str__(self):
            return f"NODE[{self.value}]"
            # NODE[들어온 value]

    def __init__(self):
        self.head = self.Node(None)
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        if self.head.next == self.head:
            return True
        else:
            return False

    def add_after(self, node, value):
        new = self.Node(value)
        n = node.next
        n.prev = new
        new.next = n
        node.next = new
        new.prev = node

    def add_before(self, node, value):
        new = self.Node(value)
        p = node.prev
        p.next = new
        new.prev = p
        node.prev = new
        new.next = node

    def add_head(self, value):
        new = self.Node(value)
        if self.head == self.head.next:
            self.head.next = new.next
            self.head.prev = new.prev
            self.head = new
            return 0
        new.next = self.head
        new.prev = self.head.prev
        self.head.prev.next = new
        self.head.prev = new
        return 0

    def add_tail(self, value):
        new = self.Node(value)
        if self.is_empty():
            self.head.prev = new
            self.head.next = new
            self.head = new
            return 0
        self.head.prev.next = new
        self.head.prev = new
        new.next = self.head
        new.prev = self.head.prev
        return 0

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_head(self):
        if self.is_empty():
            return
        self.head.prev.next = self.head.next
        self.head.next.prev = self.head.prev
        self.head.next.next.prev = self.head.next
        self.head = self.head.next

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


# 아래는 위 코드 테스트를 위해서 만들어놓은 샘플입니다. 수정하지 마세요.
# 다음과 같은 결과가 나와야 합니다.
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
    list = LinkedList()
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

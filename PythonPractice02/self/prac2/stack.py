import sys

input = sys.stdin.readline


class Stack:
    items = []

    def __init__(self):
        return

    def push(self, item):
        self.items.append(item)
        return

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def is_empty(self):
        return not self.items


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.pop())
stack.push(2)
stack.push(3)
print(stack.is_empty())
stack.push(4)
print(stack.peek())
stack.push(5)
print(stack.items)

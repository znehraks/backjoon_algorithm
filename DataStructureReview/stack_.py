class Stack:
    items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return -1
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if self.items:
            return False
        return True


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())

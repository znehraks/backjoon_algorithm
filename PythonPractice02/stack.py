class Stack:
    def __init__(self):
        self.items = []
        return

    def push(self, item):
        self.items.append(item)
        return
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return not self.items
    
    def peek(self):
        if self.items:
            return self.items[-1]


# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.peek())
# print(stack.is_empty())

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print(stack.is_empty())
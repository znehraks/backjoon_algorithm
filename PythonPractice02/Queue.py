class Queue:
    items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items:
            return self.items.pop(0)
    def is_empty(self):
        return not self.items 
    def peek(self):
        return self.items[0]

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.peek())
print(queue.pop())
print(queue.is_empty())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.is_empty())
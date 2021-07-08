# class Stack:
#     items = []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def is_empty(self):
#         return not self.items
#     def peek(self):
#         return self.items[-1]
    
# case = int(input())
# num_list = [int(input()) for _ in range(case)]
# output = []

# pointer = 0
# stack = Stack()

# for i in range(case):
#     stack.push(i+1)
#     output.append("+")

#     while(pointer < case and stack.peek() == num_list[pointer]):
#         stack.pop()
#         output.append("-")
#         pointer+=1
# if not stack.is_empty():
#     print("NO")
# else:
#     for i in output:
#         print(i)


from sys import stdin
n = int(stdin.readline())
in_ = map(lambda x : int(x.rstrip()), stdin.readlines())

def numeric():
    cnt, stack, result = 1, [], []
    for i in in_:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt+=1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)

print(numeric())
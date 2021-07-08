stack = []
N = int(input())
for i in range(N):
    a = int(input())
    if a != 0:
        stack.append(a)
    else:
        stack.pop()
print(sum(stack))
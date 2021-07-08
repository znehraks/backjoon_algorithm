stack = []
N = int(input())
for i in range(N):
    stack.clear()
    s = input()
    for index, j in enumerate(s):
        if j == "(":
            stack.append(j)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                break
        if index == len(s)-1:
            if len(stack) != 0:
                print("NO")
            else:
                print("YES")
import sys
n = int(sys.stdin.readline())
q = []
start=0
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        q.append(int(s[1]))
    elif s[0] == "pop":
        if len(q)>start:
            print(q[start])
            start += 1
        else:
            print(-1)
    elif s[0] == "size":
        print(len(q)-start)
    elif s[0] == "empty":
        if len(q)-start == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if len(q) > start:
            print(q[start])
        else:
            print(-1)
    elif s[0] == "back":
        if len(q) > start:
            print(q[-1])
        else:
            print(-1)
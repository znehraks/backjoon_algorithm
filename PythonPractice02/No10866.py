import sys
n = int(sys.stdin.readline())
d = []
for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push_front":
        d = list(reversed(d))
        d.append(int(s[1]))
        d = list(reversed(d))
    elif s[0] == "push_back":
        d.append(int(s[1]))
    elif s[0] == "pop_front":
        if d:
            print(d.pop(0))
        else:
            print(-1)
    elif s[0] == "pop_back":
        if d:
            print(d.pop(-1))
        else:
            print(-1)
    elif s[0] == "size":
        print(len(d))
    elif s[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif s[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif s[0] == "back":
        if d:
            print(d[-1])
        else:
            print(-1)
        
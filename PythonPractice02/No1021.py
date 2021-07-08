import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
d = deque()
for i in range(N):
    d.append(i+1)
want = map(int, sys.stdin.readline().split())
total = 0
for w in want:
    i = 0
    while w != d[i]:
        i+=1
    if len(d) - i < i:
        i = len(d) - i
    else:
        i = -i
    d.rotate(i)
    total += abs(i)
    d.popleft()
print(total)
import math
n = int(input())
info = []
hund, rest = 0, 0
for _ in range(n):
    info.append(input().split())
for i in info:
    if int(i[2])%int(i[0]) == 0:
        hund = int(i[0])*100
    else:
        hund = (int(i[2])%int(i[0])) * 100
    rest = math.ceil(int(i[2])/int(i[0]))
    print(hund+rest)
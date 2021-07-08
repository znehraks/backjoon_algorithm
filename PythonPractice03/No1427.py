import sys
n = sys.stdin.readline().rstrip()
list = []
for i in n:
    list.append(int(i))
list = sorted(list, reverse=True)
for i in list:
    print(i, end='')

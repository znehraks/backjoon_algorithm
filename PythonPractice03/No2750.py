n = int(input())
list = []
for _ in range(n):
    list.append(int(input()))

for i in range(len(list)):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
print(*list)

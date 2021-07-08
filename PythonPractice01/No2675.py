t = int(input())
case = []
for _ in range(t):
    case.append(input().split())
for i in case:
    for j in i[1]:
        print(j * int(i[0]), end='')
    print("")
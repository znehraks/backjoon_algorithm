n = int(input())
fives = n//5
rest = 0
result = []
for i in range(fives+1):
    rest = n - 5*i
    threes = rest//3
    for j in range(threes+1):
        if 5*i + 3*j == n:
            result.append(i+j)
if len(result) != 0:
    print(min(result))
else:
    print(-1)
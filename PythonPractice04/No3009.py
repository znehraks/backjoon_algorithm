xs = []
ys = []
for i in range(3):
    x, y = map(int, input().split(" "))
    xs.append(x)
    ys.append(y)
for i in xs:
    if xs.count(i) == 1:
        x1 = i
        break
for i in ys:
    if ys.count(i) == 1:
        y1 = i
        break
print(x1, y1)

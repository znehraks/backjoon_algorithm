import math
list = []
while True:
    n = int(input())
    if n == 0:
        break
    list.append(n)
c = [0 for _ in range(123456*2+1)]
for i, _ in enumerate(c):
    if i == 2 or i == 3 or i == 5:
        c[i] = 1
        continue
    if i % 2 == 0:
        continue
    else:
        for k in range(2, round(math.sqrt(i+1))+1):
            if i % k == 0:
                break
            if k == round(math.sqrt(i+1)):
                c[i] = 1
                break
for i in list:
    sum = 0
    for j in range(i+1, i*2+1):
        if c[j] == 1:
            sum += 1
            continue
    print(sum)

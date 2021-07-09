import math
n = int(input())
num = []
prime = [0 for _ in range(10001)]
for i in range(len(prime)):
    if i == 2 or i == 3 or i == 5:
        prime[i] = 1
        continue
    if i % 2 == 0:
        continue
    else:
        for j in range(2, round(math.sqrt(i))+1):
            if i % j == 0:
                break
            if j == round(math.sqrt(i+1)):
                prime[i] = 1
for i in range(n):
    k = int(input())
    temp = []
    for j in range(1, k):
        if prime[j] == 1 and prime[k-j] == 1:
            temp.append(j)
    while True:
        if temp[-1] > k/2:
            temp.pop()
        else:
            break
    temp.append(k-temp[-1])
    print(temp[-2], temp[-1])

n = int(input())


def func(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum + n


res = n
for i in range(n):
    if n == func(i):
        print(i)
        break
    elif i == n-1:
        print(0)

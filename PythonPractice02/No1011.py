c = int(input())
for _ in range(c):
    x, y = input().split()
    dist = int(y) - int(x)
    n=0
    while dist > n*(n+1):
        n += 1
    if((dist - (n-1)*(n))>n):
        print(2*n)
    else:
        print(2*n - 1)
    
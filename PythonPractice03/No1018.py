n, m = map(int, input().split())
for i in range(n-7):
    for j in range(m-7):
        for k in range(i, n+i):
            for l in range(j, m+j):
                print("*", end='')
            print("")

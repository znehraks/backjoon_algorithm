import math
N = int(input())

while N % 2 == 0:
    N = int(N/2)
    print(2)

while True:
    for i in range(3, N+1, 2):
        if N % i == 0:
            N = int(N/i)
            print(i)
            break
    if N == 1:
        break

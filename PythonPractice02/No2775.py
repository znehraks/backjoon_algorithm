
# 1 3
#0-1 + 0-2 + 0-3
# 2 3
#1-1 + 1-2 + 1-3
#0-1 + 0-1+0-2 + 0-1+0-2+0-3
# 3 3
#2-1 + 2-2 + 2-3
#1-1 + 1-1+1-2 + 1-1+1-2+1-3
#0-1 + 0-1+0-1+0-2 +0-1+ 0-1+0-2 +0-1+0-2+0-3
#n>1 k층 n호 인원 구할때
#k-1,1 + k-1,2 + ... + k-1,n


def cal(k, n):
    z = [[0] * (n) for i in range(k+1)]
    for i in range(k):
        for j in range(n):
            if i == 0:
                z[i][j] = j+1
    for i in range(k):
        for j in range(n):
            if i != 0:
                z[i][j] = sum(z[i-1][:j+1])
    return z

n = int(input())
case = []
for _ in range(n):
    k = int(input())
    n = int(input())
    z = cal(k,n)
    print(sum(z[k-1]))


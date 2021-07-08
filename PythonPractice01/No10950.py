N = int(input())
result=[]
for _ in range(N):
    A, B = input().split()
    A = int(A)
    B = int(B)
    result.append(A+B)
for i in result:
    print(i)
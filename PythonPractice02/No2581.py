m = int(input())
n = int(input())
result = []
for i in range(m,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
        if j == i-1:
           result.append(i)
if 2 >= m and n >=2:
    result.append(2)
if len(result) !=0:
    print(sum(result))  
    print(min(result))
else:
    print(-1) 
n = int(input())
nums = list(map(int, input().split()))
ctn = 0
result = []
length = 0
for i in nums:
    for j in range(2,i):
        if i != 2 and i%j == 0:
            ctn = 1
            break
        if j == i-1:
            result.append(i)
if 2 in nums:
    length = len(result) + 1
else:
    length = len(result)
print(length)

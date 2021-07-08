# 1  ==1
# 2-7 == 6
# 8-19 == 12
# 20 -37 == 18
#         24
#         30

# n - 1
# 0
# 1-6
# 7-18
# 19-36
# 37-60
# ...
n = int(input())
ctn = 0
while n > 3*ctn**2+3*ctn+1:
    ctn += 1
if n==1:
    print(1)
else:
    print(ctn+1)
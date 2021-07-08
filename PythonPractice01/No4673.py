#d(n)을 구한다음 10000에서 빼기
def d(n):
    n = str(n)
    sum=0
    for i in n:
        sum += int(i)
    return sum + int(n)
num = list(range(1,10000)) 
d_list = []
for i in num:
    if d(i) < 10000:
        d_list.append(d(i))

for i in d_list:
    if i in num:
        num.remove(i)

for i in num:
    print(i)
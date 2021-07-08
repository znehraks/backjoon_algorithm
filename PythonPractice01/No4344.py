n = int(input())
case = []
sum = 0.000
avgs = []
count = 0
for _ in range(n):
    case.append(list(map(int, input().split())))
for i, v in enumerate(case):
    for j, k in enumerate(v):
        if j != 0:
            sum += k
        if j == len(v)-1:
            avgs.append(float(sum/(len(v)-1)))
            sum = 0
for i, v in enumerate(case):
    for j, k in enumerate(v):
        if j != 0 and k > avgs[i]:
            count += 1
        if j == len(v)-1:
            print("%.3f%%"%(round(count/(len(v)-1)*100,3)))
            count = 0
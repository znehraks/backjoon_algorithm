import collections
a = list(input().upper())
c = collections.Counter(a)
c_max = []
for i, j in c.items():
    if j == max(c.values()):
        c_max.append(i)
        if len(c_max) > 1:
            print('?')
            break
if len(c_max) == 1:
    print(c_max[0])
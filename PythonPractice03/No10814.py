n = int(input())
p = []
for i in range(n):
    age, name = input().split()
    p.append([int(age), i, name])

p = sorted(p)
for i in p:
    print(i[0], i[2])

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i],a[j]=a[j],a[i]
for i in a:
    print(i)
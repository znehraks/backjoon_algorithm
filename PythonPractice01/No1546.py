n = int(input())
a = list(map(int,input().split()))
new = []
for i in a:
    new.append(i/max(a)*100)
print(sum(new)/n)

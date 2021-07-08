a, b = map(int, input().split())
def changer(n):
    h = n//100
    t = (n%100)//10
    o = n%10
    return o*100 + t*10 + h
if changer(a) > changer(b):
    print(changer(a))
else:
    print(changer(b))
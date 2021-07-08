a, b, c = map(int, input().split())
try:
    num = a // (c-b) + 1 
except:
    num = -1
if num < 0 or c-b < 0:
    num = -1
print(num)
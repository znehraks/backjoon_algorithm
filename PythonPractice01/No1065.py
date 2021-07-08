n = int(input())
def func(n):
    count = 0
    if n < 10 and n >= 1:
        count += n
    elif n < 100 and n >= 10:
        count += n
    elif n >= 100:
        count += 99
        for i in range(100, n+1):
            if int(str(i)[1])*2 == int(str(i)[0])+int(str(i)[2]):
                count += 1
    return count
print(func(n))
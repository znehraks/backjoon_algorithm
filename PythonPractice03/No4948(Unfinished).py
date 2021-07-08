import math


def isPrime(num):
    if num == 1:
        return False
    n = int(math.sqrt(num))
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True


def primeCount(n):
    token = 0
    for i in range(n, n*2+1):
        if isPrime(i):
            token += 1
    return token


while True:
    n = int(input())
    print(primeCount(n))
    if n == 0:
        break

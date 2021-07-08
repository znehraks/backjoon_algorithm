import timeit
import sys

sys.setrecursionlimit(150000000)

def po(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
print(po(2,7))

# 2 2 2 2 2 2 2
# 2 4 4 4
# 2 4 16

# 2 2 2 2 2 2
# 4 4 4
# 4 16
def po2(x, n):
    if n%2 == 0:
        return po2(x*x, n//2)
    else:
        if n == 1:
            return x
        else:
            return x * po2(x*x, n//2)

print(po2(2, 7))

def po3(x,n,count=0):
    if n == 0:
        return 1
    else:
        return x * po3(x, n-1)

print(po3(2, 7))

# for i in range(0, 11):
#     print(f'2^{i}=\t{po(2,i)}\t{po2(2,i)}')


# print(timeit.timeit(f'{po(2, 1000)}', 'from __main__ import po', number = 100))
# print(timeit.timeit(f'{po2(2, 1000)}', 'from __main__ import po2', number = 100))
# print(timeit.timeit(f'{po3(2, 1000)}', 'from __main__ import po3', number = 100))

# print(timeit.timeit(f'{po(2, 3000)}', 'from __main__ import po', number = 100))
# print(timeit.timeit(f'{po2(2, 3000)}', 'from __main__ import po2', number = 100))
# print(timeit.timeit(f'{po3(2, 3000)}', 'from __main__ import po3', number = 100))

# a =     b = timeit.timeit(f'factorial2({i})', 'from __main__ import factorial2')
#     print

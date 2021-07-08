import timeit

# iterative type


def f1(n):
    nums = list(range(n, 0, -1))
    result = 1
    for i in nums:
        result *= i
    return result

# recursive type


def f2(n):
    if n>0:
        return n * f2(n-1)
    return 1


for i in range(30):
    a = timeit.timeit(f'f1({i})', 'from __main__ import f1')
    b = timeit.timeit(f'f2({i})', 'from __main__ import f2')
    print(f'{i}! = {f1(i)} ({a}) ? {f2(i)} ({b})')



# import timeit


# def factorial1(n):
#     if n > 0:
#         return factorial1(n - 1) * n
#     return 1


# def factorial2(n):
#     sum = 1
#     for i in range(1, n + 1):
#         sum = sum * i
#     return sum

# for i in range(20):
# a = timeit.timeit(f'factorial1({i})', 'from __main__ import factorial1')
# b = timeit.timeit(f'factorial2({i})', 'from __main__ import factorial2')
# print(i, a, b, (b/a))

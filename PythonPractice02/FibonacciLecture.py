import functools
#iterative 
# O(n)
# O(1)
#0 1 1 2 3 5 8


def fibo_iterative(n):
    fibo=[0, 1]
    for i in range(2,n):
        fibo.append(fibo[i-2]+ fibo[i-1])
    return fibo[len(fibo)-1]

def fibo_iterative_pro(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

#recursive 
# O(2^n)

@functools.lru_cache(maxsize=1000)
def fibo_recursive(n):
    if n == 1 or n == 0:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)

#recursive_fix
#Dynamic Programming:
# Problem -> Sub-problem + Memoize
# O(n)
# space O(n)
def fibo_recursive_2(n):
    global cache
    if cache[n]:
        return cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo_recursive_2(n-1) + fibo_recursive_2(n-2)
    cache[n] = result
    return result

cache = [None for _ in range(1000)]

for i in range(100):
    # print(fibo_recursive(i))
    # print(i,fibo_iterative_pro(i))
    print(i,fibo_recursive_2(i))
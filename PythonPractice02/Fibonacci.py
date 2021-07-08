#학번: 60152572
#이름: 유정민

#iterative
#worst-case's time-complexity: O(n)
def fibonacci_iterative(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
    return a

#recursive
#worst-case's time-complexity: O(2^n)
def fibonacci_recursive(n):
    if n == 1 or n == 0:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#recursive-memoization
#worst-case's time-complexity: O(n)
cache = [None for _ in range(100)]
def fibonacci_recursive_memoization(n):
    global cache
    if cache[n]:
        return cache[n]
    elif n == 0 or n == 1:
        result = n
    else:
        result = fibonacci_recursive_memoization(n-1) + fibonacci_recursive_memoization(n-2)
    cache[n] = result
    return result

print(fibonacci_recursive_memoization(6))
N = int(input())
result = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    result.append(a+b)
for i, v in enumerate(result):
    print(f"Case #{i+1}: {v}")
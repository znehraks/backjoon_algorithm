s = input()
alpha = list(range(97,123))
result = []
for v in alpha:
    if chr(v) in s:
        location = s.index(chr(v))
        result.append(f'{location}')
    else:
        result.append('-1')
for i in result:
    print(i,end=' ')
n = int(input())
case = []
count = 0
score = 0
scores = []
fore = ""
for _ in range(n):
    case.append(str(input()))

for index, value in enumerate(case):
    for j, v in enumerate(value):
        if v == 'O':
            if j == 0:
                count = 1
                score += count
                fore = v
            if j != 0:
                if fore == 'O':
                    count += 1
                    score += count
                    fore = v
                else:
                    count = 1
                    score += count
                    fore = v
        else:
            fore = v
        if j == len(value)-1:
            scores.append(score)
            score = 0
            count = 0
for i in scores:
    print(i)
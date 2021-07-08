scores = []
sum = 0
for _ in range(5):
    scores.append(int(input()))
for i in scores:
    if i < 40:
        i = 40
    sum += i
print(sum//5)
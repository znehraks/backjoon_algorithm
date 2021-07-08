count = 0
n = int(input())
for i in range(n):
    word = input()
    count+=list(word) == sorted(word, key=word.find)
print(count)
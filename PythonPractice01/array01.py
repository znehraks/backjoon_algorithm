#팩토리얼
num = input("수를 입력: " )
result = 1
for i in range(1,int(num)+1):
    result *= int(i)

print(num,"i = ", result)
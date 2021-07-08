array = [0,4,2,1,5,6,8,7,9,3]

number = input("수 입력: ")

for i in array:
    if int(number) == i:
        print("성공")
        break
    elif array.index(i) == len(array)-1:
        print("실패")
        
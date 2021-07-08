original = int(input())
count = 0


def func(num):
    global original
    global count
    if (original == num) and (count != 0):
        print(count)
        return
    num = str(num)
    sum_part = 0
    for i in num:
        sum_part += int(i)
    sum_part %= 10
    new_num = int(num[-1])*10 + sum_part
    count += 1
    func(new_num)


func(original)

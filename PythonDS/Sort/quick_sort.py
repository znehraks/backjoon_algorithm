'''
학번: 60152572
이름: 유정민
'''


def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    less = []
    equal = []
    greater = []
    for i in list:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    return quick_sort((less))+equal+quick_sort((greater))


list = [1, 8, 5, 2, 9, 3, 7, 10, 6, 4]
print(quick_sort(list))

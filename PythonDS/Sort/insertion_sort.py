'''
Insertion Sort
학번:60152572
이름:유정민
'''


def insertion(data):
    for i in range(len(data)):
        for j in range(i, 0, -1):
            if j == 0:
                break
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            # print("i", i)
            # print(data)
    return data


data = [5, 9, 6, 1, 3, 2, 7, 4, 8]
data = insertion(data)
print(data)

'''
Bubble Sort
학번:60152572
이름:유정민
'''


def bubble(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
            # print(data)
    return data


data = [5, 9, 6, 1, 3, 2, 7, 4, 8]
data = bubble(data)
print(data)

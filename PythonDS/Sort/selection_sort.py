'''
Selection Sort
학번:60152572
이름:유정민
'''


def selection(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                data[j], data[min_idx] = data[min_idx], data[j]
        # print(data)
    return data


data = [5, 9, 6, 1, 3, 2, 7, 4, 8]
data = selection(data)
print(data)

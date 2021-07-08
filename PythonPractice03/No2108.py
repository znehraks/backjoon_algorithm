import sys
from collections import Counter
list = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
sorted_list = sorted(list)


def mode(x):
    mode_dict = Counter(x)
    modes = mode_dict.most_common()
    if len(x) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod


print(round(sum(list)/len(list)))
print(sorted_list[len(sorted_list)//2])
print(mode(sorted_list))
print(max(list)-min(list))

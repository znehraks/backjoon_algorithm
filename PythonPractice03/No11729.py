K = int(input())
print_list = []


def hanoi(num, a, b, c, print_list):
    if(num == 1):
        print_list.append([a, c])
        return None

    hanoi(num - 1, a, c, b, print_list)
    print_list.append([a, c])
    hanoi(num - 1, b, a, c, print_list)


hanoi(K, 1, 2, 3, print_list)

print(len(print_list))
for a, b in print_list:
    print('{} {}'.format(a, b))

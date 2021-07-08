n, m = map(int, input().split())
v = list(map(int, input().split()))


def blackjack(n, list):
    temp = [0, 0, 0]
    res = 0
    for i in range(len(list)):
        temp[0] = list[i]
        for j in range(i+1, len(list)):
            temp[1] = list[j]
            for k in range(j+1, len(list)):
                temp[2] = list[k]
                if m-sum(temp) == 0:
                    return sum(temp)
                elif abs(m - res) > abs(m-sum(temp)) and sum(temp) < m:
                    res = sum(temp)
                if i == n-3 and k == n-1:
                    return res


print(blackjack(n, v))

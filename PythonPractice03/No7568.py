n = int(input())
person_info = [list(map(int, input().split())) for _ in range(n)]

rank_list = [1]*n

for i in range(len(person_info)):
    for j in range(len(person_info)):
        if person_info[i][0] != person_info[j][0] and person_info[i][1] != person_info[j][1]:
            if (person_info[i][0] > person_info[j][0]) and (person_info[i][1] > person_info[j][1]):
                rank_list[j] += 1

print(*rank_list)

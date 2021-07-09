import math
n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    dist_c = math.sqrt((x2-x1)**2+(y2-y1)**2)
    dist_r_sum = r1+r2
    dist_r_sub = abs(r1-r2)

    # 중심이 같을 때
    if dist_c == 0:
        # 반지름이 같으면
        if dist_r_sub == 0:
            print(-1)
        # 반지름 다르면
        else:
            print(0)
    # 중심이 다를 때
    else:
        # 접할 때
        if dist_c == dist_r_sum or dist_c == dist_r_sub:
            print(1)
        # 교차할때
        elif dist_c < dist_r_sum and dist_c > dist_r_sub:
            print(2)
        # 중심간 거리가 반지름 길이 합보다 클때
        else:
            print(0)

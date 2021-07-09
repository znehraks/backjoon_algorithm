while True:
    x, y, z = map(int, input().split(" "))
    if x == 0 and y == 0 and z == 0:
        break
    list = sorted([x, y, z])
    if list[0]**2 + list[1]**2 == list[2]**2:
        print("right")
    else:
        print("wrong")

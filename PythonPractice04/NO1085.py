import math
x, y, w, h = map(int, input().split(" "))
width_ = x
height_ = y
width = w-x
height = h-y
dia = round(math.sqrt((w-x)**2 + (h-y)**2))
print(min([width_, height_, width, height, dia]))

n = int(input())
line = 0
while n > (line**2+line)/2:
    line += 1
if line%2 == 1:
    print(f"{int(1+(line**2+line)/2-n)}/{int(line-((line**2+line)/2-n))}")
else:
    print(f"{int(line-((line**2+line)/2-n))}/{int(1+(line**2+line)/2-n)}")
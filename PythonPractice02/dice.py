import random as r
even = 0
six_factor = 0
count = 0
while count < 100000:
    num = r.randrange(1,7)
    if num % 2 == 0:
        even += 1
        if 6 % num == 0:
            six_factor += 1
    count += 1

perc = six_factor / even
print(perc)
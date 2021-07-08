burgers = []
bever = []
burgermin = 2000
bevermin = 2000
for _ in range(3):
    burgers.append(int(input()))
for _ in range(2):
    bever.append(int(input()))
for i in burgers:
    if i < burgermin:
        burgermin = i
min = 2000
for i in bever:
    if i < bevermin:
        bevermin = i
print(burgermin+bevermin - 50)

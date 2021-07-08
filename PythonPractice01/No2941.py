s = input()
words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in words:
    s = s.replace(i,"*")
print(len(s))
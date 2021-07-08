H, M = input().split()
H = int(H)
M = int(M)
#M이 45보다 클때,작을때
#H가 0일때, 아닐때
if H == 0:
    if M < 45:
        M = 60 - (45 - M)
        H = 23
    elif M >= 45 and M <= 59:
        M = M - 45
else:
    if M < 45:
        M = 60 - (45 - M)
        H = H - 1
    elif M >= 45 and M <= 59:
        M = M - 45
print(H, M)
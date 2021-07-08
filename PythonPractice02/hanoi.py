#O(2^n)
step = 0
def move(disk, src, dest):
    global step
    step += 1
    print(f"disk {disk}: move from [{src}] to [{dest}]")
def hanoi(n, src, dest, tmp):
    if n > 0:
        hanoi(n-1, src, tmp, dest)
        move(n, src, dest)
        hanoi(n-1, tmp, dest, src)

print("10 Disk from A to B")
print("======================")    
hanoi(10, "A", "C", "B")
print(f"{step} steps")
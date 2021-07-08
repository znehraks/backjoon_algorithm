nums = []
for _ in range(10):
    nums.append(int(input())%42)
nums = list(set(nums))
print(len(nums))
# nums = []
# max=0
# seq=0
# for _ in range(9):
#     nums.append(int(input()))
# for i, v in enumerate(nums):
#     if v > max:
#         max = v
#         seq = i+1
# print(f"{max}\n{seq}")
nums = []
for _ in range(9):
    nums.append(int(input()))
print(max(nums))
print(nums.index(max(nums))+1)
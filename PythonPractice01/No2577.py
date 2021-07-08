# nums = []
# counts = []
# count = 0
# a=1
# for _ in range(3):
#     nums.append(int(input()))
# for i in nums:
#     a *= i
# a = sorted(str(a))
# for i, v in enumerate(range(10)):
#     for j, k in enumerate(a):
#         if str(v) == k:
#             count += 1
#         if j == len(a)-1:
#             counts.append(count)
#             count = 0


a=int(input())
b=int(input())
c=int(input())
k = a*b*c
k_list = list(str(k))
for i in range(10):
    k_num_count = k_list.count(str(i))
    print(k_num_count)

# ex = [0,0,0,2,2,2,3,3,3,3,3]
# for i in range(10):
#     ex_num_count = ex.count(i)
#     print(ex_num_count)

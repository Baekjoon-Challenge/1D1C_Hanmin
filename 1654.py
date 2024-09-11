import sys

kn = list(map(int,sys.stdin.readline().split()))
nums = []

for i in range(kn[0]):
    nums.append(int(sys.stdin.readline()))
overall = sum(nums)
ceiling = overall // kn[1]  
save = nums[:]

for j in range(kn[1] - kn[0] + 1):
    if save[i]//(j+1) < ceiling:
        nums.append(max(save)//(j+1))

nums = list(nums)
nums.sort(reverse =True)

for i in nums:
    line = 0
    for j in save:
        line += j//i
    if line == kn[1]:
        break
    
print(i)
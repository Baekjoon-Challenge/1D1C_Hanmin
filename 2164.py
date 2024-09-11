import sys
from collections import deque

n = int(sys.stdin.readline())
nums = [i+1 for i in range(n)]
nums = deque(nums)
cnt = 0
while 1:
    if len(nums) == 1:
        break
    if cnt%2 == 0:
        nums.popleft()
    else:
        nums.append(nums.popleft())
    cnt += 1
        
print(nums[0])
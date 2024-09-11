import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

arr = [[0,0] for i in range(41)] 
arr[0] = [1,0]
arr[1] = [0,1]
for i in range(2,41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]
    
for i in nums:
    print(arr[i][0], arr[i][1])
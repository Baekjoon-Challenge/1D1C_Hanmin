import sys
import math

mn = list(map(int,sys.stdin.readline().split()))

arr = [i for i in range(0,mn[1]+1)]
k = 2

for i in range(2, int(math.sqrt(mn[1]))+1):
    if arr[i] == 0:
        continue
    
    for j in range(i*2, mn[1]+1, i):
        arr[j] = 0
        
        
for i in range(mn[0],mn[1]+1):
    if arr[i] != 0 and arr[i] != 1:
        print(arr[i])
    
    

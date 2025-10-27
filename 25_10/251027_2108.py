import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

avg = round(sum(arr)/N)
arr.sort()
if N%2 == 0:
    median = round((arr[N//2] + arr[N//2-1])/2,1)  
else:
    median = arr[N//2]

counter = Counter(arr)
mode_list=[]
for i, j in counter.items():
    if max(counter.values()) == j:
        mode_list.append(i)

if len(mode_list) == 1:
    mode = mode_list[0]
else:
    mode = mode_list[1]
ran = arr[-1] - arr[0]
print(avg)
print(median)
print(mode)
print(ran)

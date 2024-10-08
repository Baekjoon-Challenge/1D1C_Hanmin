import sys

N = int(sys.stdin.readline())

arr = [[0,0,0]]
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,N+1):
    arr[i][0] += (min(arr[i-1][1],arr[i-1][2]))
    arr[i][1] += (min(arr[i-1][0],arr[i-1][2]))
    arr[i][2] += (min(arr[i-1][0],arr[i-1][1]))


print(min(arr[N]))
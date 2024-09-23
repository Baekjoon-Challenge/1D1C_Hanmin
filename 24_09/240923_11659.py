import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

sum_arr = [0]
sum = 0
for i in range(N):
    sum +=arr[i]
    sum_arr.append(sum)

for i in range(M):
    start, end = map(int,sys.stdin.readline().split())
    print(sum_arr[end]-sum_arr[start-1])
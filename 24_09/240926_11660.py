import sys

N , M= map(int,sys.stdin.readline().split())
arr = [[0 for i in range(N+1)]]
sum_arr = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(N):
    line = [0] + list(map(int,sys.stdin.readline().split()))
    arr.append(line)
    
for i in range(1, N+1):
    for j in range(1,N+1):
        sum_arr[i][j] = sum_arr[i][j-1] + sum_arr[i-1][j] - sum_arr[i-1][j-1] + arr[i][j]



for i in range(M):
    x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2]-sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])


    
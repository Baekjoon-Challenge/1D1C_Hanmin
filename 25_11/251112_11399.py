import sys
input = sys.stdin.readline

N = int(input())
time_list = list(map(int,input().split()))

time_list.sort()
min_time = 0
for i in range(N):
    min_time += sum(time_list[:i+1]) 

print(min_time)
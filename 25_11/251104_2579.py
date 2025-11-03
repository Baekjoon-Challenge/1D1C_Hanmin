import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]

for i in range(N):
    stairs.append(int(input()))

dp = [0 for _ in range(N+1)]
dp[1] = stairs[1]
if N > 1:
    dp[2] = stairs[1] + stairs[2]
if N > 2:
    for i in range(3,N+1):
        dp[i] = stairs[i] + max(stairs[i-1]+dp[i-3],dp[i-2])


print(dp[N])



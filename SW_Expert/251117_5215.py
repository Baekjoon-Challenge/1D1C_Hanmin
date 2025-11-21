
T = int(input())

for i in range(1,T+1):
    N, L = map(int,input().split())
    
    val = [0]
    cal = [0]
    for j in range(N):
        T, K = map(int,input().split())
        val.append(T)
        cal.append(K)
        
    dp = [[0 for _ in range(L+1)] for _ in range(N+1)]
    for j in range(N+1):
        for k in range(L+1):
            if j==0 or k==0:
                dp[j][k] = 0

            elif cal[j] <= k:
                dp[j][k] = max(val[j]+dp[j-1][k-cal[j]],dp[j-1][k])
                

            else:
                dp[j][k] = dp[j-1][k]
    print("#%d %d" %(i,dp[N][L]))
import sys

wt = []
val = []

N, K = map(int,sys.stdin.readline().split())

for i in range(N):
    W, V = map(int,sys.stdin.readline().split())
    wt.append(W)
    val.append(V)


def knapsack(K, wt, val, N):
    arr =[[0 for i in range(K+1)]for j in range(N+1)]

    for i in range(N+1):
        for w in range(K+1):
            if i==0 or w==0:
                arr[i][w] = 0
            elif wt[i-1] <= w:
                arr[i][w] = max(val[i-1]+arr[i-1][w-wt[i-1]],arr[i-1][w])
            else:
                arr[i][w] = arr[i-1][w]

    return arr[N][K]

print(knapsack(K,wt,val,N))
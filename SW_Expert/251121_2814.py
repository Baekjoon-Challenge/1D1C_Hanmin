T = int(input())

def dfs(start, visited, length):
    global answer
    answer = max(answer,length)
    visited[start] = True
    for v in adj[start]:
        if not visited[v]:
            dfs(v,visited,length+1)
    visited[start] = False



for case in range(1,T+1):
    N, M = map(int,input().split())
    adj = [[]for _ in range(N+1)]

    for i in range(M):
        x, y = map(int,input().split())
        adj[x].append(y)
        adj[y].append(x)

    answer = 0
    for i in range(1,N+1):
        visited = [False for _ in range(N + 1)]
        dfs(i,visited,1)

    print(f"#{case} {answer}")

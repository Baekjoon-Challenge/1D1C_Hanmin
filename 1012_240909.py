import sys
T = int(input())
sys.setrecursionlimit(10**6)
def dfs(graph, x, y):
    graph[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        if graph[x+dx[i]][y+dy[i]]==1:
            dfs(graph, x+dx[i], y+dy[i])
    return

cnt_list = []
for i in range(T):
    m, n, k = map(int,input().split())
    graph = [[0]*(m+1) for _ in range(n+1)]
    
    for j in range(k):
        x, y = map(int,input().split())
        graph[y][x] = 1

        
    cnt = 0
    for h in range(n):
        for l in range(m):
            if graph[h][l] == 1:
                dfs(graph, h, l)
                cnt += 1

    cnt_list.append(cnt)
    
for i in cnt_list:
    print(i)
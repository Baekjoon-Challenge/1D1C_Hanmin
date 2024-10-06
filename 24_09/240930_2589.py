import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))



dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(graph, y, x):
    visited = [[-1 for i in range(m)] for j in range(n)]
    queue = deque()
    queue.append([y,x])
    visited[y][x] = 0
    cnt = 0
    while queue:
        v = queue.popleft()

        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 'L' and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[v[0]][v[1]]+1
                    cnt = max(cnt,visited[ny][nx])
                    queue.append([ny,nx])
    return cnt

max_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            max_cnt = max(max_cnt,bfs(graph,i,j))

        

print(max_cnt)
import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: graph[i][j] = -1

def bfs(graph, y, x):
    queue = deque()
    graph[y][x] = 0
    queue.append([y,x])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    

    while queue:
        v =  queue.popleft()
        for i in range(4):
            ny = dy[i] + v[0]
            nx = dx[i] + v[1]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[v[0]][v[1]] + 1
                    queue.append([ny,nx])

def start(graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                bfs(graph,i,j)
                return
            
start(graph)
for i in range(n):
    for j in range(m):
        print(graph[i][j], end =" ")
    print()




        
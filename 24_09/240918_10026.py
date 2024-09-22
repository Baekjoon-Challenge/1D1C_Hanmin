from collections import deque
import sys
import copy

def bfs(graph, y, x, cnt, color):
    graph[y][x] = cnt
    queue.append([y,x])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == color:
                    graph[ny][nx] = cnt
                    queue.append([ny,nx])

def redgreen_bfs(graph, y, x, cnt):
    graph[y][x] = cnt
    queue.append([y,x])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == "R" or graph[ny][nx] == "G":
                    graph[ny][nx] = cnt
                    queue.append([ny,nx])


N = int(sys.stdin.readline())

graph = []
color_graph = []
for i in range(N):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))

color_graph = copy.deepcopy(graph)

queue = deque()
#normal people
cnt = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            bfs(graph,i,j,cnt,"R")
            cnt+=1
        elif graph[i][j] == "B":
            bfs(graph,i,j,cnt,"B")
            cnt+=1
        elif graph[i][j] == "G":
            bfs(graph,i,j,cnt,"G")
            cnt+=1
normal_cnt = max(map(max,graph))

cnt = 1
for i in range(N):
    for j in range(N):
        if color_graph[i][j] == "R" or color_graph[i][j] == "G":
            redgreen_bfs(color_graph,i,j,cnt)
            cnt+=1
        elif color_graph[i][j] == "B":
            bfs(color_graph,i,j,cnt,"B")
            cnt+=1

color_cnt = max(map(max,color_graph))

print(normal_cnt, color_cnt)
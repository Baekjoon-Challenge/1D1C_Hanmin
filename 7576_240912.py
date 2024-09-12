from collections import deque

def bfs(graph, queue):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 0:
                    queue.append([ny,nx])
                    graph[ny][nx] = graph[v[0]][v[1]] + 1

def max_day(graph):
    day = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1  
            if graph[i][j] > day:
                day = graph[i][j]
    return day-1

M, N = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))


queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

bfs(graph, queue)

print(max_day(graph))








    
from collections import deque

def bfs(graph, queue):
    dz = [0,0,0,0,1,-1]
    dy = [1,-1,0,0,0,0]
    dx = [0,0,1,-1,0,0]

    while queue:
        v = queue.popleft()
        for i in range(6):
            nz = v[0]+dz[i]
            ny = v[1]+dy[i]
            nx = v[2]+dx[i]
            if 0<=nz<H and 0<=ny<M and 0<=nx<N:
                if graph[nz][ny][nx] == 0:
                    queue.append([nz,ny,nx])
                    graph[nz][ny][nx] = graph[v[0]][v[1]][v[2]] + 1

def max_day(graph):
    day = 0
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if graph[i][j][k] == 0:
                    return -1  
                if graph[i][j][k] > day:
                    day = graph[i][j][k]
    return day-1




N, M, H = map(int, input().split())

graph = []
for i in range(H):
    square = []
    for j in range(M):
        square.append(list(map(int,input().split())))
    graph.append(square)

queue = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])

bfs(graph, queue)


print(max_day(graph))









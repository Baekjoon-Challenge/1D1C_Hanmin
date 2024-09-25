import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))


def bfs(graph, y, x, cnt):
    graph[y][x] = cnt
    queue = deque()
    queue.append([y,x])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx] == "1":
                    graph[ny][nx] = cnt
                    queue.append([ny,nx])

cnt = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            bfs(graph,i,j,cnt)
            cnt += 1

print(cnt-1)

cnt_list= [0 for i in range(cnt-1)]
for i in range(cnt-1):
    for j in range(N):
        for k in range(N):
            if graph[j][k] == i+1:
                cnt_list[i] += 1
cnt_list.sort()

for i in cnt_list:
    print(i)

from collections import deque
import copy
def bfs(graph, y, x, cnt_graph):
    queue = deque()
    queue.append([y,x])
    graph[y][x] = 0
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx] == 1:
                    queue.append([ny,nx])
                    graph[ny][nx] = 0
                    cnt_graph[ny][nx] = cnt_graph[v[0]][v[1]]+1
                    


N, M = map(int,input().split())

graph = []

for i in range(N):
    l = list(input())
    line = [int(_) for _ in l]
    graph.append(line)
cnt_graph = copy.deepcopy(graph)
bfs(graph,0,0,cnt_graph)

print(cnt_graph[-1][-1])


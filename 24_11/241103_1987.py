import sys
from collections import deque
R, C = map(int,sys.stdin.readline().split())


graph = []
for i in range(R):
    graph.append(list(sys.stdin.readline().rstrip()))

num_graph= [[0 for i in range(C)] for j in range(R)]

def DFS(graph,y,x,visited,depth):
    global ans
    stack = set()
    stack.add((y,x,visited+graph[y][x],depth))

    while stack:
        nowy, nowx, nowvisited, nowdepth = stack.pop()
        ans = max(ans, nowdepth)
        for i in range(4):
            ny = nowy + dy[i]
            nx = nowx + dx[i]
            if 0<=ny<R and 0<=nx<C:
                if graph[ny][nx] not in nowvisited:
                    stack.add((ny,nx,nowvisited+graph[ny][nx],nowdepth+1))
    return

ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

DFS(graph,0,0,'',1)

print(ans)





    

        



import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

MAX = 100001
graph = [-1 for i in range(MAX)]
visit = [0 for i in range(MAX)]

def bfs(graph,visit,N):
    graph[N] = 0
    visit[N] = 1
    queue = deque()
    queue.append(N)

    while queue:
        v = queue.popleft()
        for i in [v-1,v+1,2*v]:
            if 0<=i<MAX:
                if graph[i] == -1:
                    graph[i] = graph[v]+1
                    visit[i] = visit[v]
                    queue.append(i)
                elif graph[i] == graph[v]+1:
                    visit[i] += visit[v]


bfs(graph,visit,N)

print(graph[K])
print(visit[K])

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

MAX = max(N,K) * 2

graph = [-1 for i in range(MAX)]

def bfs(graph, N):
    queue = deque()
    graph[N] = 0
    queue.append(N)
    while queue:
        v = queue.popleft()
        dx =[v+1, v-1, v*2]
        for i in dx:
            if 0<=i<MAX:
                if graph[i] == -1:
                    graph[i] = graph[v] + 1
                    queue.append(i)

bfs(graph,N)

print(graph)

print(graph[K])


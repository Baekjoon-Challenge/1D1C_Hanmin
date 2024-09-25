from collections import deque
import sys

N, K = map(int,sys.stdin.readline().split())

MAX =max(N,K)*2
graph = [-1 for i in range(MAX)]

def bfs(graph, N):
    queue = deque()
    graph[N] = 0
    queue.append(N)
    while queue:
        v = queue.popleft()
        nx = [v+1,v-1]
        if 0<=2*v<MAX:
            if graph[2*v] == -1 or graph[2*v] > graph[v]:
                graph[2*v] = graph[v]
                queue.appendleft(2*v)
        for i in nx:
            if 0<=i<MAX:
                if graph[i] == -1:
                    graph[i] = graph[v]+1
                    queue.append(i)
        


bfs(graph,N)

print(graph[K])
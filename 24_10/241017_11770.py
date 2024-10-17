import sys
import heapq

INF = 1e9

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
for i in range(m):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])




def dijkstra(graph, start,end):
    parent=[-1 for i in range(n+1)]
    distance = [INF for i in range(n+1)]
    distance[start] = 0
    q = []
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                parent[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
    print(distance[end])

    path = []
    p = end
    while p != start: 
        path.append(p)
        p = parent[p]
    path.append(start)
    path.reverse()

    print(len(path))
    print(*path)

start, end = map(int, sys.stdin.readline().split())
dijkstra(graph,start,end)
    




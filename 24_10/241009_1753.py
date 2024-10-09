import sys
import heapq

V, E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for i in range(V+1)]
INF = 1e9
for i in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])


q=[]
distance = [INF for i in range(V+1)]
def dijkstra(start):  
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)
for i in range(1,V+1):
    if i == K:
        print("0")
    else:
        dist = distance[i]
        if dist >= INF: print("INF")
        else: print(dist)


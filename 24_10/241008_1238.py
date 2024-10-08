import sys
import heapq

inf =1e9

n, m, x = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])

q = []
def dijkstra(start, end):
    distance = [inf for i in range(n+1)]
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[end]

max_dist = 0
for i in range(1,n+1):
    if i == x: continue
    cur_dist = dijkstra(i,x)+dijkstra(x,i)
    if cur_dist>max_dist:
        max_dist = cur_dist

print(max_dist)
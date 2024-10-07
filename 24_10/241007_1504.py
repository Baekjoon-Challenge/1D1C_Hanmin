import sys
import heapq


n, e = map(int,sys.stdin.readline().split())
inf = 1e9

graph = [[] for i in range(n+1)]

for i in range(e):
    start, end, w = map(int,sys.stdin.readline().split())
    graph[start].append([end,w])
    graph[end].append([start,w])

first, second = map(int,sys.stdin.readline().split())

q = []
def dijkstra(start,end):
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

way1 = 0
way1+=dijkstra(1,first)
way1+=dijkstra(first,second)
way1+=dijkstra(second,n)


way2 = 0
way2+=dijkstra(1,first)
way2+=dijkstra(first,second)
way2+=dijkstra(second,n)

ans = min(way1,way2)
if ans >= inf:
    print("-1")
else:
    print(ans)


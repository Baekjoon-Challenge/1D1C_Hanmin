import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = 10000000*n

distance = [inf for i in range(n+1)]
visited = [False for i in range(n+1)]
graph = [[] for j in range(n+1)]
for i in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append([end, cost]) 

s, e = map(int,sys.stdin.readline().split())



def dijkstra(start,end):
    distance[start] = 0
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = min(distance[i[0]],i[1])
    if visited[e] == True:
        return
    
    while visited[end] != True:
        min_dis = inf
        index = 0
        for i in range(1,n+1):
            if visited[i] == True: continue
            if distance[i] < min_dis:
                min_dis = distance[i]
                index = i
        visited[index] = True
        for j in graph[index]:
            distance[j[0]] = min(distance[index] + j[1],distance[j[0]])
        



dijkstra(s,e)

print(distance[e])
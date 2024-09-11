from collections import deque

def dfs(graph, start, visited):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return
  
def bfs(graph, start, visited):
    queue = deque([start])
    visited.append(start)

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in visited:
                queue.append(node)
                visited.append(node)


n, m , v = map(int,input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort()

    
#DFS
visited = []
dfs(graph, v, visited)
for i in visited:
    print(i,end=" ")
print()

#BFS
visited = []
bfs(graph, v, visited)
for i in visited:
    print(i,end=" ")
print()

    



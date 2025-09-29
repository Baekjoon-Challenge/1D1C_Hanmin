import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,graph,visited):
    q = deque()
    q.append(s)
    visited[s] = 1
    
    while(q):
        now = q.popleft()
        for next in graph[now]:
            if visited[next]:
                continue      
            q.append(next)
            visited[next] = 1


n,m  = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph2[y].append(x)
    
s,t = map(int, input().split())

visit1 = [0]*(n+1)
visit1[t] = 1
bfs(s,graph,visit1)
visit2 = [0]*(n+1)
visit2[s] = 1
bfs(t,graph,visit2)

visit1_re = [0]*(n+1)
bfs(s,graph2,visit1_re)
visit2_re = [0]*(n+1)
bfs(t,graph2,visit2_re)

answer = 0
for i in range(1, n+1):
    if i == s or i == t: 
        continue
    if visit1[i] and visit2[i] and visit1_re[i] and visit2_re[i]: 
        answer += 1

print(answer)
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
V = int(input())
relation = [[] for _ in range(N+1)]

for i in range(V):
    A, B = map(int,input().split())
    relation[A].append(B)
    relation[B].append(A)

def bfs(start):
    queue = deque([start])
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    while queue:
        com = queue.popleft()
        for i in relation[com]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return sum(visited) - 1

print(bfs(1))
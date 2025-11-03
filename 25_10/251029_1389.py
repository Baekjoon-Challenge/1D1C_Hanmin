import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
friend_list = [[] for _ in range(N+1)]


for i in range(M):
    friendA, friendB = map(int,input().split())
    friend_list[friendA].append(friendB)
    friend_list[friendB].append(friendA)

def bfs(start):
    num = 1
    visit = [0 for _ in range(N+1)]
    queue = deque([start])
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in friend_list[v]:
            if i != start and visit[i]==0:
                queue.append(i)
                visit[i] += visit[v]+1
    return sum(visit)

        

min = N*N
min_person = 0
for i in range(1,N+1):
    num_bacon = bfs(i)
    if num_bacon < min:
        min = num_bacon
        min_person = i

print(min_person)




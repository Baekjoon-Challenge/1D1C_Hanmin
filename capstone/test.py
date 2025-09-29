import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j,color):
    x =i-1
    y =j-1

    cij = image[x][y]
    image[x][y] = color

    q = deque([[x,y]])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0)]:
            nx = x + dx
            ny = y + dy
            if 0<= nx < h and 0<= ny <w:
                if image[nx][ny] == cij:
                    image[nx][ny] = color
                    q.append([nx,ny])





h, w = map(int, input().split())
image = [list(map(int, input().split())) for i in range(h)]

q = int(input())
for i in range(q):
    i, j, c = map(int,input().split())
    bfs(i,j,c)

for i in image:
    for j in i:
        print(j,end=" ")
    print
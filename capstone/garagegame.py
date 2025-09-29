import sys
from collections import deque

n = int(input())
board = [[[] for _ in range(n)] for _ in range(3)]
for _ in range(3*n):
    for i,x in enumerate(map(int,input().split())):
        board[0][i].append(x)

for i in range(n): 
    board[0][i].reverse()

dx,dy = [0,1,0,-1],[1,0,-1,0]

def near_same_color(rnd): 
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i+1<n and board[rnd][i][j]==board[rnd][i+1][j]:
                ret[i][j]=ret[i+1][j]=1
            if j+1<n and board[rnd][i][j]==board[rnd][i][j+1]:
                ret[i][j]=ret[i][j+1]=1
    return ret

def bfs(rnd): 
    cluster = [[0 for _ in range(n)] for _ in range(n)]
    vidx = 1
    cluster_size = [0]
    score = [0]
    near_ret = near_same_color(rnd)
    for i in range(n):
        for j in range(n):
            mx,my,Mx,My = i,j,i,j
            if not near_ret[i][j]:
                cluster[i][j]=vidx
                cluster_size.append(1)
                score.append(2)
                vidx+=1
            elif not cluster[i][j] and board[rnd][i][j]:
                cluster[i][j]=vidx
                q = deque([(i,j)])
                cnt = 1
                while q:
                    x,y = q.pop()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<n and \
                            not cluster[nx][ny] and \
                            board[rnd][nx][ny]==board[rnd][i][j]:
                            mx,my=min(mx,nx),min(my,ny)
                            Mx,My=max(Mx,nx),max(My,ny)
                            cluster[nx][ny]=vidx
                            cnt += 1
                            q.append((nx,ny))
                cluster_size.append(cnt)
                score.append(cnt + (abs(mx-Mx)+1)*(abs(my-My)+1))
                vidx+=1
    return cluster, cluster_size, score

def select(cluster_idx, cluster, rnd): 
    board[rnd+1]=[b[:] for b in board[rnd]]
    for i in range(n):
        temp = []
        for j in range(len(board[rnd][i])):
            if j<n and cluster[i][j]==cluster_idx:
                continue
            temp.append(board[rnd][i][j])
        board[rnd+1][i]=temp

ans = 0
def dfs(score, step):
    global ans
    cluster, cluster_size, scores = bfs(step)
    if step==2:
        ans = max(ans,score+max(scores))
        return
    for i in range(1,len(cluster_size)):
        select(i,cluster,step)
        dfs(score+scores[i],step+1)

dfs(0,0)
print(ans)
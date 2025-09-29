import sys

input = sys.stdin.readline

def dfs(points, depth):
    if (depth == m):
        result.append(points)
        return
    
    if (points[-1] == checkpoints[depth]):
        dfs(points, depth + 1)
        return

    for i in range(4):
        ny = points[-1][0] + dY[i]
        nx = points[-1][1] + dX[i]
        
        if (ny < 0 or nx < 0 or ny >= n or nx >= n):
            continue
        
        if (mat[ny][nx] == 1):
            continue

        if [ny, nx] not in points:
            dfs(points + [[ny, nx]], depth)


dY = [1, 0, -1, 0]
dX = [0, 1, 0, -1]

n, m = map(int, input().split())
mat = []
checkpoints = []
result = []

for i in range(n):
    mat.append(list(map(int, input().split())))

for i in range(m):
    y, x = map(int, input().split())
    checkpoints.append([y-1, x-1])

dfs([checkpoints[0]], 0)

print(len(result))
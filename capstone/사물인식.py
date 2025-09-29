import sys
sys.setrecursionlimit(1000000000)

input = sys.stdin.readline

N,K = map(int,input().split())

def dfs(S, maxX, minX, maxY, minY):
    global minSize
    if S == K+1:
        nowSize = (maxX - minX) * (maxY - minY)
        if nowSize < minSize:
            minSize = nowSize
        return
    for X, Y in stack[S]:
        newMaxX = max(maxX, X) 
        newMinX = min(minX, X)
        newMaxY = max(maxY, Y) 
        newMinY = min(minY, Y)
        newSize = (newMaxX - newMinX) * (newMaxY - newMinY)
        if newSize < minSize:
            dfs(S+1, newMaxX, newMinX, newMaxY, newMinY)


minSize = 4000000
stack = [[] for _ in range(K+1)]
for i in range(N):
    x,y,color = map(int, input().split())
    stack[color].append((x,y))
for x, y in stack[1]:
    dfs(2,x,x,y,y)
print(minSize)


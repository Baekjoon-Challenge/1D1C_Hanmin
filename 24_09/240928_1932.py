import sys

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == i:
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j],graph[i-1][j-1])


print(graph)
print(max(graph[n-1]))
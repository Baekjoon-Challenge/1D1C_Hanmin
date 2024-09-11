import sys

edges = []
while 1:
    edges.append(list(map(int,sys.stdin.readline().split())))
    if edges[-1] == [0,0,0]:
        edges.pop()
        break
    
for i in edges:
    sq_edge = []
    for j in i:
        sq_edge.append(j**2)
    sq_edge.sort()
    max_sq = sq_edge.pop()
    if max_sq == sum(sq_edge):
        print("right")
    else:
        print("wrong")
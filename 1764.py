import sys
line = list(map(int,sys.stdin.readline().split()))
n = line[0]
m = line[1]
heard = set([])
seen = set([])
for i in range(n):
    heard.add(sys.stdin.readline())
    
for j in range(m):
    seen.add(sys.stdin.readline())
    
intersect = heard.intersection(seen)

intersect = list(intersect)
intersect.sort()
print(len(intersect))
for i in intersect:
    print(i,end="")
print()
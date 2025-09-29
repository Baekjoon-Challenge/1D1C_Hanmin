import sys
from collections import deque

input = sys.stdin.readline
H, K, R = map(int, input().split())
works = [deque(map(int, input().split())) for _ in range(2**H)] 
staffcnt = 2**(H+1) - 1 
organ = [deque() for _ in range(staffcnt+1)]  
for i in range(len(works)):
    organ[staffcnt-i] = works[-i-1] 
notEndStaff = 2**(H) 
complete = 0
for day in range(R):
    for t in range(1, notEndStaff): 
        if t == 1:
            if len(organ[1]) != 0: 
                complete += organ[1].popleft()
        if day % 2 == 1 : 
            if len(organ[t*2]) != 0:
                organ[t].append(organ[t*2].popleft())
        elif day % 2 == 0 : 
            if len(organ[t*2+1]) != 0:
                organ[t].append(organ[t*2+1].popleft())
        
print(complete)
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
ans = [-1]*n
road = {'A':deque(), 'B':deque(), 'C':deque(), 'D':deque()}

rightCar = {'A':'D', 'B':'A', 'C':'B', 'D':'C'}


for i in range(n):
    t, w = input().split()
    road[w].append((int(t), i))

    if i == 0:
        currTime = int(t)

maxV = 1000000001


while road['A'] or road['B'] or road['C'] or road['D']:

    minV = maxV
    minVisited = {'A':0, 'B':0, 'C':0, 'D':0}
    isCar = {'A':False, 'B':False, 'C':False, 'D':False}

    isDeadlock = 0


    for p in ['A', 'B', 'C', 'D']:
        if road.get(p):
            t, _ = road[p][0]
            minVisited[p] = t

            minV = min(minV, t)

            if t <= currTime:
                isDeadlock += 1

        else:
            minVisited[p] = maxV

    if isDeadlock == 4:
        break
    if isDeadlock == 0:
        currTime = minV


    for p in ['A', 'B', 'C', 'D']:

        if minVisited[p] <= currTime:

            if road.get(rightCar[p]):
                if minVisited[rightCar[p]] > currTime:
                    isCar[p] = True
            else:
                isCar[p] = True

    for p in ['A', 'B', 'C', 'D']:
        if isCar[p]:
            _, num = road[p].popleft()
            ans[num] = currTime

    currTime += 1
        

for k in ans:
    print(k)
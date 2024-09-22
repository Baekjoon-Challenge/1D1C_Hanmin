import heapq
import sys

abs_heap = []

N = int(sys.stdin.readline())

for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(abs_heap,(abs(x),x))

    else:
        if not abs_heap:
            print("0")
        else:
            v = heapq.heappop(abs_heap)[1]
            print(v)




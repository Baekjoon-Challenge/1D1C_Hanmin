import heapq
import sys

min_heap = []

N = int(sys.stdin.readline())
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not min_heap:
            print("0")
        else:
            v = heapq.heappop(min_heap)
            print("v")
    else:
        heapq.heappush(min_heap,x)
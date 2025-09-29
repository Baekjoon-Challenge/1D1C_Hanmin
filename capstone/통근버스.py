import sys

input = sys.stdin.readline
n = int(input())
bus = list(map(int, input().split()))

t, result = 0, 0

for i in range(n) :
    for j in range(i + 1, n) :
        if bus[i] < bus[j] :
            t += 1
        else :
            result += t
    t = 0

print(result)
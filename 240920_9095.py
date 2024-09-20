import sys

ways = [0 for i in range(11)]
ways[1] = 1
ways[2] = 2
ways[3] = 4


def dp_ways(num, ways):
    if num < 4:
        return ways[num]
    else:
        ways[num] = dp_ways(num-1,ways)+ dp_ways(num-2,ways)+ dp_ways(num-3,ways)
        return ways[num]
    

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    print(dp_ways(n,ways))
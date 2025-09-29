import sys

input = sys.stdin.readline
def check(mid):
    cost = 0
    for i in power:
        if mid > i:
            cost += (mid - i) ** 2
    if cost <= b:
        return True
    else:
        return False

def search(start, end):
    if start == end:
        return start
    mid = (start + end + 1) // 2
    if check(mid):
        return search(mid, end)
    else:
        return search(start, mid - 1)

n, b = map(int, input().split())
power = list(map(int, input().split()))
power.sort()
min_power = power[0]
answer = search(min_power, 2 * 10 ** 9)
print(answer)
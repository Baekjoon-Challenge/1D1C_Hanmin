import sys

def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start + end)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            end = mid -1
        elif target > data[mid]:
            start = mid + 1
    return False

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

for i in nums:
    if binary_search(i, a):
        print("1")
    else:
        print("0")
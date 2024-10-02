import sys

N, M = map(int,sys.stdin.readline().split())

arr = [i+1 for i in range(N)]

def back_track(arr,M):
    result = []
    if M == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in back_track(arr[i:],M-1):
            result.append([elem]+rest)

    return result


for i in back_track(arr,M):
    for j in i:
        print(j,end = " ")
    print()
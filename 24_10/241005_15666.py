import sys

N, M = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

def back_track(arr,M):
    result = []
    if M == 0:
        return [[]]
    else:
        for i in range(len(arr)):
            elem = arr[i]
            if i != 0 and elem == arr[i-1]: continue
            for rest in back_track(arr[i:],M-1):
                result.append([elem]+rest)
    
    return result


for i in back_track(arr,M):
    for j in i:
        print(j,end=" ")
    print()




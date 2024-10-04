import sys
import copy

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
            if i>0 and elem == arr[i-1]: continue
            new_arr = copy.deepcopy(arr)
            del new_arr[i]
            for rest in back_track(new_arr,M-1):
                sequence = [elem]+rest
                result.append(sequence)
    return result


for i in back_track(arr,M):
    for j in i:
        print(j,end = " ")
    print()
    

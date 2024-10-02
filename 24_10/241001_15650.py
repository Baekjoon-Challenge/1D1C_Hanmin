import sys

N, M = map(int,sys.stdin.readline().split())

arr = [i+1 for i in range(N)]

def combination(arr,r):
    result = []
    if r == 0:
        return[[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:],r-1):
            result.append([elem] + rest)
        
    return result

for i in combination(arr,M):
    for j in i:
        print(j,end = " ")
    print()

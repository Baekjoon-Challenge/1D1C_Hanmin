import sys

arr = [0,0,1,1,2]
for i in range(5, 10**6+1):
    if i%3 == 0 and i%2 == 0:
        arr.append(min(arr[i//2]+1, arr[i//3]+1))
    elif i%2 == 0:
        arr.append(min(arr[i//2]+1, arr[i-1]+1))
    elif i%3 == 0:
        arr.append(min(arr[i//3]+1, arr[i-1]+1))
    else:
        arr.append(arr[i-1]+1)
    

n = int(sys.stdin.readline())

print(arr[n])
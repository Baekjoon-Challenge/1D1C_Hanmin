import copy
import sys
M = int(sys.stdin.readline())

arr = [0 for i in range(21)]

for i in range(M):
    line = sys.stdin.readline().rstrip()
    if line == "all":
        arr = [1 for i in range(21)]
        continue
    elif line == "empty":
        arr = [0 for i in range(21)]
        continue
    else:
        l = line.split()
        op = l[0]
        num = int(l[1])
    

    if op == "add":
        if arr[num] == 0:
            arr[num] = 1
    elif op == "remove":
        if arr[num] == 1:
            arr[num] = 0
    elif op == "check":
        if arr[num] == 1:
            print("1")
        else:
            print("0")
    elif op == "toggle":
        if arr[num] == 1:
            arr[num] = 0
        else:
            arr[num] = 1
    

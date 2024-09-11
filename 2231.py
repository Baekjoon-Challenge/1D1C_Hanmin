import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    str_i = str(i)
    arr = list(map(int,str_i))
    if (i + sum(arr)) == n:
        print(i)
        exit(0)
    
print(0)
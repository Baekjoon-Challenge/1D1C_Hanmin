import sys

n = int(sys.stdin.readline())
fac = 1
for i in range(1,n+1):
    fac = fac * i
    
fac = str(fac)
fac = fac[::-1]


cnt = 0
for i in range(len(fac)):
    if fac[i] != "0":
        break
    cnt += 1

print(cnt)

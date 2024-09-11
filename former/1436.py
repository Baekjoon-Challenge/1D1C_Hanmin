import sys

n = int(sys.stdin.readline())
flag = 0
i = 666
while 1:
    num = str(i)
    if num.find("666") != -1:
        flag += 1
    if flag == n:
        break
    i += 1
print(i)
    
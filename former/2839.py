import sys
n = int(sys.stdin.readline())
num_5 = n // 5
num_3 = 0
while 1:
    remain = n - 5 * num_5
    if remain % 3 == 0:
        num_3 = remain // 3
        break
    elif num_5 == 0:
        num_5 = -1
        num_3 = 0
        break
    else:
        num_5 -= 1
        
print(num_5 + num_3)
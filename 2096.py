import sys

n = int(sys.stdin.readline())
line = list(map(int,sys.stdin.readline().split()))
minimum = line[:]
temp = line[:]
for i in range(n-1):
    next_line = list(map(int,sys.stdin.readline().split()))
    for j in range(3):
        if j == 1:
            middle = line[j] + next_line[j]
            right = line[j+1] + next_line[j]
            left = line[j-1] + next_line[j]
            l_middle = minimum[j] + next_line[j]
            l_right = minimum[j+1] + next_line[j]
            l_left = minimum[j-1] + next_line[j]
            next_line[j] = max(middle,right,left)
            temp[j] = min(l_left, l_right, l_middle)
        elif j == 0:
            middle = line[j] + next_line[j]
            right = line[j+1] + next_line[j]
            l_middle = minimum[j] + next_line[j]
            l_right = minimum[j+1] + next_line[j]
            next_line[j] = max(middle,right)
            temp[j] = min(l_right, l_middle)
        else:
            middle = line[j] + next_line[j]
            left = line[j-1] + next_line[j]
            l_middle = minimum[j] + next_line[j]
            l_left = minimum[j-1] + next_line[j]
            next_line[j] = max(middle,left)
            temp[j] = min(l_left, l_middle)
    line = next_line[:]
    minimum = temp[:]

print(max(line),min(minimum))
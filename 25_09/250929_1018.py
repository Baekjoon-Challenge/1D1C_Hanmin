import sys

input = sys.stdin.readline
N, M = map(int,input().split())

chessboard = []
for i in range(N):
    chessboard.append(list(input().rstrip()))

min_change = 1000
for h in range(N-7):
    for w in range(M-7):
        change = 0
        #첫 시작이 W
        start = "W"
        for i in range(h,h+8):
            check = start
            for j in range(w,w+8):
                if chessboard[i][j] != check:
                    change += 1
                if check == "W":
                    check = "B"
                else:
                    check = "W"
            if start == "W":
                start = "B"
            else:
                start = "W"
        if change < min_change:
            min_change = change

for h in range(N-7):
    for w in range(M-7):
        change = 0
        #첫 시작이 B
        start = "B"
        for i in range(h,h+8):
            check = start
            for j in range(w,w+8):
                if chessboard[i][j] != check:
                    change += 1
                if check == "W":
                    check = "B"
                else:
                    check = "W"
            if start == "W":
                start = "B"
            else:
                start = "W"
        if change < min_change:
            min_change = change


print(min_change)
T = int(input())

for case in range(1,T+1):
    H, W = map(int,input().split())
    field = []
    for i in range(H):
        field.append(list(input()))
    N = int(input())
    command = list(input())
    x = 0
    y = 0

    for i in range(H):
        for j in range(W):
            if field[i][j] == "^" or field[i][j] == "<" or field[i][j] == ">" or field[i][j] == "v":
                x = i
                y = j

    for i in command:
        if i == "U":
            field[x][y]="^"
            if x - 1>=0:
                if field[x-1][y] ==".":
                    field[x][y], field[x-1][y] = field[x-1][y], field[x][y]
                    x -= 1

        elif i == "D":
            field[x][y] = "v"
            if x + 1 < H:
                if field[x + 1][y] == ".":
                    field[x][y], field[x + 1][y] = field[x + 1][y], field[x][y]
                    x += 1

        elif i == "L":
            field[x][y] = "<"
            if y - 1 >= 0:
                if field[x][y-1] == ".":
                    field[x][y], field[x][y-1] = field[x][y-1], field[x][y]
                    y -= 1

        elif i == "R":
            field[x][y] = ">"
            if y + 1 < W:
                if field[x][y+1] == ".":
                    field[x][y], field[x][y+1] = field[x][y+1], field[x][y]
                    y += 1

        elif i == "S":
            if field[x][y] == "^":
                bomb_x = x
                while 1:
                    if field[bomb_x][y]=="#":
                        break
                    if field[bomb_x][y]=="*":
                        field[bomb_x][y] = "."
                        break
                    if bomb_x == 0:
                        break
                    bomb_x -= 1

            elif field[x][y] == "v":
                bomb_x = x
                while 1:
                    if field[bomb_x][y]=="#":
                        break
                    if field[bomb_x][y]=="*":
                        field[bomb_x][y] = "."
                        break
                    if bomb_x == H-1:
                        break
                    bomb_x += 1

            elif field[x][y] == "<":
                bomb_y = y
                while 1:
                    if field[x][bomb_y] == "#":
                        break
                    if field[x][bomb_y] == "*":
                        field[x][bomb_y] = "."
                        break
                    if bomb_y == 0:
                        break
                    bomb_y -= 1

            elif field[x][y] == ">":
                bomb_y = y
                while 1:
                    if field[x][bomb_y] == "#":
                        break
                    if field[x][bomb_y] == "*":
                        field[x][bomb_y] = "."
                        break
                    if bomb_y == W-1:
                        break
                    bomb_y += 1

    for i in range(H):
        if i == 0:
            print(f"#{case} {''.join(field[i])}")
        else:
            print(f"{''.join(field[i])}")






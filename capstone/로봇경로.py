import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())
hist = [[''] * w for _ in range(h)]
check = [[False] * w for _ in range(h)]
head = {(-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3}
pos = ['^', '>', 'v', '<']
answer = ''

for i in range(h):
    tmp = sys.stdin.readline()
    for j in range(w):
        hist[i][j] = tmp[j]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
candidate = []
for i in range(h):
    for j in range(w):
        if hist[i][j] == '.':
            continue
        count = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
                if hist[nx][ny] == '#':
                    count += 1
        if count == 1:
            candidate.append((i, j))

start_point, end_point = candidate[0], candidate[1]
now_point = start_point
now_head = ' '
def check_head(answer, point, prev_head):
    i, j = point
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
            if hist[nx][ny] == '#' and not check[nx][ny]:
                next_point = (nx, ny)
                now_head = head[(nx - i, ny - j)]
                check[i + dx[k]][j + dy[k]] = True
                check[i + 2 * dx[k]][j + 2 * dy[k]] = True
                if prev_head == ' ' or prev_head == now_head:
                    answer += 'A'
                else:
                    if pos[prev_head - 1] == pos[now_head]:
                        answer += 'LA'
                    else:
                        answer += 'RA'
                return answer, (i + 2 * dx[k], j + 2 * dy[k]), now_head

print(f'{start_point[0] + 1} {start_point[1] + 1}')
answer, now_point, now_head = check_head(answer, now_point, now_head)
print(pos[now_head])

while now_point != end_point:
    answer, now_point, now_head = check_head(answer, now_point, now_head)
print(answer)
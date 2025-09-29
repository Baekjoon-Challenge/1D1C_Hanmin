from collections import deque

# 이미지 프로세싱 함수 - BFS 사용
def ImageProcessing(image, i, j, c):

    y = i - 1
    x = j - 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    cij = image[y][x]

    # 픽셀의 색상이 바꾸고 싶은 색상과 같은 경우
    if cij == c:
        return image
    else:
        image[y][x] = c

    my_queue = deque([[y, x]])

    while my_queue:
        y, x = my_queue.popleft()
        for a in range(4):
            ny = y + dy[a]
            nx = x + dx[a]

            if (0 <= ny < len(image)) and (0 <= nx < len(image[0])):
                if image[ny][nx] == cij:
                    image[ny][nx] = c
                    my_queue.append([ny, nx])
    
    return image

# h x w 크기의 이미지 입력받기
h, w = map(int, input().split())
image = [list(map(int, input().split())) for i in range(h)]

# main
Q = int(input())
for num in range(Q):
    i, j, c = map(int, input().split())
    image = ImageProcessing(image, i, j, c)

# 결과 출력하기
for i in image:
    print(" ".join(map(str, i)))
def row_check(start,r,length):
    left = start
    right = start + length -1
    while left < right:
        if arr[r][left]!=arr[r][right]:
            return False
        left+=1
        right-=1
    return True
def col_check(start,c,length):
    top = start
    bot = start + length -1
    while top < bot:
        if arr[top][c]!=arr[bot][c]:
            return False
        top+=1
        bot-=1
    return True


for tc in range(10):
    case = int(input())
    arr = []
    answer = 1
    for i in range(100):
        arr.append(list(input()))
    found = False
    for length in range(100,0,-1):
        for r in range(100):
            for start in range(0,100-length+1):
                if row_check(start,r,length):
                    answer = length
                    found = True
                    break
            if found:
                break
        if found:
            break

        for c in range(100):
            for start in range(0, 100 - length + 1):
                if col_check(start, c, length):
                    answer = length
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(f"#{case} {answer}")







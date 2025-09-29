import sys

# 실제 애플리케이션이 사용가능한 메모리 900MiB

N = int(input())

for i in range(N):
    T = int(input())
    app = list(map(int, input().split()))

    app.sort()
    start = 0
    end = T-1
    cnt = 0

    # 주어지는 값은 300 - 900 사이로 이루어져 있다.
    # 300, 301-599, 600, 601-900
    # 601-900 사이의 값은 항상 혼자서만 서버를 한대 차지한다.
    while(start <= end and 601 <= app[end] <= 900):
        cnt += 1
        end -= 1
    
    # 600은 300과 짝을 지어서내보낸다.
    # 300이 더이상 없다면 600은 그냥 혼자만 서버를 차지
    while(start < end and app[end] == 600 and app[start] == 300):
        cnt += 1
        start += 1
        end -= 1
	
    # 남은 300의 갯수 카운트
    cnt_300 = 0 
    while start <= end and app[start] == 300:
        cnt_300 += 1
        start += 1

    # 301 - 599, 600까지의 숫자는 그 내부에서 제일 처음 값과 마지막 값을 짝지어준다.
    while start < end:
        if app[start] + app[end] <= 900:
            cnt += 1
            start += 1
            end -= 1
        elif cnt_300 != 0:
            cnt += 1
            cnt_300 -= 1
            end -= 1
        # 900 초과인 경우 
        else:
            cnt += 1
            end -= 1
    
    # 해당 범위의 값이 1개 남았을 때 300쪽으로 눈을 돌려 있다면 짝을 이루고 아니면 혼자
    if start == end:
        cnt += 1
        if cnt_300 != 0:
            cnt_300 -= 1    
            
    #print("!start, end, cnt :", start, end, cnt)
    
    if cnt_300 != 0:
        cnt += (cnt_300+2)//3
    print(cnt)
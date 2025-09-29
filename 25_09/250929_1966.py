import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    queue = list(map(int,input().split()))
    cnt = 1
    while(1):
        if len(queue) == 1:
            break
        if M == 0:
            if queue[0] < max(queue[1:]):
                queue.append(queue.pop(0))
                M = len(queue)-1
                
            else:
                break
        else:
            if queue[0] < max(queue[1:]):
                queue.append(queue.pop(0))
                M = M - 1
                
            else:
                queue.pop(0)
                cnt += 1
                M = M - 1
                
    print(cnt)


            
    
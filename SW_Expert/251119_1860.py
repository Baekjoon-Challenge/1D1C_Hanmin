T = int(input())

for case in range(1,T+1):
    N, M, K = map(int,input().split())
    arrive = list(map(int,input().split()))
    arrive.sort()
    flag = True
    for i in range(N):
        make_cnt = arrive[i]//M
        if make_cnt == 0:
            flag = False
            break
        bang = make_cnt*K
        if i+1 > bang:
            flag = False
            break

    if flag:
        print(f"#{case} Possible")
    else:
        print(f"#{case} Impossible")


        

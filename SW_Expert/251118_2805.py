T = int(input())
for case in range(1,T+1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(list(map(int,input())))
    # if N == 1:
    #     print("#%d %d" %(case,farm[0][0]))
    #     continue
    profit = 0
    half = N//2
    margin = half
    for i in range(N):
        profit += sum(farm[i][margin:N-margin])
        if i < half:
            margin -= 1
        else:
            margin += 1
    
    print("#%d %d" %(case,profit))
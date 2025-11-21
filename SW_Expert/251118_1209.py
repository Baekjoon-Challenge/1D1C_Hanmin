for i in range(1,11):
    num = int(input())
    arr = []
    for j in range(100):
        arr.append(list(map(int,input().split())))
    
    sum_list = []
    for j in range(100):
        sum_list.append(sum(arr[j]))

    
    for j in range(100):
        cnt_sum = 0
        for k in range(100):
            cnt_sum += arr[k][j]
        sum_list.append(cnt_sum)

    up_cnt = 0
    for j in range(100):
        up_cnt+=arr[j][j]
    sum_list.append(up_cnt)
    down_cnt = 0
    for j in range(100):
        down_cnt += arr[j][99-j]
    sum_list.append(down_cnt)

    print("#%d %d" %(i,max(sum_list)))
    
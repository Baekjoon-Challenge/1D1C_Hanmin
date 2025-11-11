import sys
input = sys.stdin.readline

for i in range(10):
    N = int(input())
    building_list = list(map(int, input().split()))
    view_cnt =0
    for j in range(2,N-2):
        max_near = max(building_list[j-2],building_list[j-1],building_list[j+1],building_list[j+2])
        if max_near>=building_list[j]:
            continue
        else:
            view_cnt += (building_list[j]-max_near)

    print("#%d %d" %(i+1,view_cnt))
        

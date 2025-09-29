import sys

n,m = map(int,input().split())
meeting_room_reserve_dic = {}

for i in range(n):
    room = input()
    # 미팅룸의 예약 시간을 계수를 이용하여 표현한다.(딕셔너리를 이용한다.)
    meeting_room_reserve_dic[room] = [0]*18

for i in range(m):
    # 룸, 시작 시간, 끝나는 시간을 각각 저장한다.
    room, start, end = input().split()
    start = int(start)
    end = int(end)
    # 예약이 되어있는 시간에 1을 채워 넣는다.
    for j in range(start,end):
        meeting_room_reserve_dic[room][j] =1
# 딕셔너리를 이름 순서대로 저장한다.
meeting_room_reserve_list = sorted(meeting_room_reserve_dic.items())

# 여기 부터는 예약이 없는 시간을 찾는 부분이다.
# 회의실의 수만큼 for문을 돌린다.
for i in range(n):
    # 여기서 first=1 은 처음 시간을 체크하는지 확인하는 부분이다.
    first =1
    # 빈회의실 시간을 저장하는 리스트이다. 
    time = []
    # 9시부터 18시까지 회의실 시간을 체크한다.
    for j in range(9,18):
        # 미팅룸 시간이 비어있고 만약에 이 회의실을 체크하는 것이 처음이라면 first= 1인지 확인한다.
        if meeting_room_reserve_list[i][1][j] ==0 and first == 1:
            # 여기서 빈시간을 체크하고
            not_reserve_s= j
            # 체크를 했으므로 first=0으로 변경해준다.
            first = 0
        # 미팅룸 시간이 차있으면 1이므로 그리고 첫 방문이 아니기 때문에 first=0인지 확인한다.
        elif meeting_room_reserve_list[i][1][j] ==1 and first ==0:
            # 미팅룸 시간이 비어있는 마지막 시간을 저장한다.
            not_reserve_f = j
            # 다시 first를 1로 변환해준다.
            first = 1
            # 여기서 time에 비어있는 시작시간과 끝나는 시간을 저장해준다.
            time.append([not_reserve_s,not_reserve_f])
    # 이부분은 마지막에 비어있는 시간이 끝까지 지속 될때 사용되는 부분으로 알고 있으면 된다.
    if first == 0 :
        time.append([not_reserve_s,18])

    print('Room {}:'.format(meeting_room_reserve_list[i][0]))
    if len(time)==0:
        print("Not available")
    else:
        print("{} available:".format(len(time)))

        for k in range(len(time)):
            print("{0:02d}-{1}".format(time[k][0],time[k][1]))
    if i != (n-1):
        print("-----")